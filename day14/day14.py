import os
import timeit
import re
from itertools import product


# ideas
# part1: loop through lines, if mask then set mask. otherwise, split value in memloc and value. convert value to bit. apply bitmask. sum memory.
# part2: loop through lines, first apply mask to position, then do floating bit generation and update the memory positions


def log(*args):
    if LOGGING:
        for i in args:
            print( str(i) )

def timefunc(iter, function, *args):
    def wrap():
        function(*args)
    t = timeit.Timer(wrap)
    return t.timeit(iter) / iter #average


def gen_combinations(s):
    keyletters = '10'
    res = []
    # Convert input string into a list so we can easily substitute letters
    seq = list(s)

    # Find indices of key letters in seq
    indices = [ i for i, c in enumerate(seq) if c == 'X']

    # Generate key letter combinations & place them into the list
    for t in product(keyletters, repeat=len(indices)):
        for i, c in zip(indices, t):
            seq[i] = c
        res.append(''.join(seq))
    return res


def solve1(d, part2=False):
    mem = {}
    
    #regex for pos and val
    pat = re.compile('\[(\d+)\] = (\d+)')
    for l in d:
        if l[:4] == 'mask': #bitmask updates
            mask = l[7:]            
            ##option 3: mask2 = dict([(pos,char) for pos,char in enumerate(mask) if char != 'X'])
        
        else: #memory position updates
            #parsing values
            vals = re.findall(pat, l)[0]
            pos, val = int(vals[0]), int(vals[1])
            log(f'pos {pos} and val {val}')

            val_b = ('0' * 36 + format(val,'b'))[-36:] #leftfill with zeros
            log(f'binary val: {val_b}')

            if part2:
                pos_b = ('0' * 36 + format(pos,'b'))[-36:] #leftfill with zeros
                log(f'binary pos: {pos_b}')

                #apply initial mask to binary position masked
                bpm = ''.join([v if m == '0' else m for m, v in zip(mask,pos_b)])
                
                #creating multiple memory positions for floating bits
                bpms = gen_combinations(bpm)
                log(f'generated { len(bpms) } positions:\n {bpms}')

                for pm in bpms: 
                    #back to memory position
                    pmi = int(pm, 2)
                    #update mem
                    mem[pmi] = val

            if not part2:
                # option 1: apply bitmask to value with zip
                bvm = ''.join([v if m == 'X' else m for m, v in zip(mask,val_b)])

                ''' #option2 : loop through range and append to string
                bvm = ''
                for i in range(36):
                    if mask[i] == 'X':
                        bvm += val_b[i]
                    else:
                        bvm += mask[i]
                '''
            
                log(f'binary value masked {bvm}')

                # 2bit binary converted back to int
                vm = int(bvm, 2)

                #update value in mem 
                mem[pos] = vm

    return sum(mem.values())

LOGGING =  0

f_loc = 'D:/GIT/AOC2020-1/day14/input.txt'
#set = {}, list = [], generator = ()
#data = [int(x)  for line in open(f_loc, 'r').read().rstrip().split("\n") for x in line.split(',') if x != 'x' ] #or read().splitlines() 
#data = [x for line in open(f_loc, 'r').read().rstrip().split("\n") for x in line.split(',') ]
data = [line for line in open(f_loc, 'r').read().rstrip().split("\n") ]
#data = list(map(char_to_int, open(f_loc, 'r').readlines()))
#i = dict(enumerate(data))

#part 1: bitmask changes the value that is written to memory.
print('\n---- part 1 ----')
print(f': {solve1(data[:])}') 
# 14954914379452

#part 2: instead of changing values, the bitmask changes memory locations, and writes the value to those locations. 
print('\n---- part 2 ----')
print(f': {solve1(data[:], part2=True)}')  
# 3415488160714


# timeit
#print(f'timeit: {timefunc(10, solve1, data, True)}' )          
# part 1: 0.043s
# part 2: 1.325s



