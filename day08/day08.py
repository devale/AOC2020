import os
import re
import timeit

# ideas
# read file with a locator, so we can jump positions. seek()
# use simple string parsing since positions are fixed.

def log(s):
    if LOGGING:
        print( str(s) )

def timefunc(iter, function, *args):
    def wrap():
        function(*args)
    t = timeit.Timer(wrap)
    return t.timeit(iter) / iter #average

def open_file(f_loc, sep='\n'):
    with open(f_loc, mode='r') as f:
        f_list = f.read().split(sep)  #better than readlines() as it removes \n
        #f_list = f.read().splitlines() #better than readlines() as it removes \n

        #splitting must be done manually, as groups are separated by a blank line. first on groups later on rows.
        #f_text = f.read().rstrip().split('\n\n')    #rstrip because it ends with a new line and split into groups.
        #f_list = [i.split('\n') for i in f_text] #split groups on rows to get list of lists.
    return f_list

#part 1
def check_loop(i):
    lines_done = set()
    acc, linenum, try_count = 0, 0, 0
  
    last_linenum = len(i) - 1 #zero index
    list_of_nop_jmp = set()
    
    while linenum not in lines_done:
        lines_done.add(linenum)
        line = i[linenum]
        #log(line)
        line = line.split(" ")
        instr = line[0]
        #log(instr)
        num = int(line[1])
        #log(num)
        if instr == 'jmp': 
            list_of_nop_jmp.add(linenum)
            linenum += num  
        elif instr=='nop':
            list_of_nop_jmp.add(linenum)
            linenum += 1
        if instr == 'acc': 
            acc += num 
            linenum += 1
        
        try_count += 1
        #log(f'new linenum = %d' % linenum)
        if try_count == 10000:
            print('max tries reached')
            break
        if linenum == last_linenum:
            print('found exit!')
            break

    log(f'loop found at line %d and accumulator %d' % (linenum, acc) )
    
    return acc, linenum, list_of_nop_jmp

def change_loop(i, res):

    try_count = 0
    list_of_nop_jmp = list(res[2]) #copy of list, for timeit iterations

    while True and try_count < 1000: #loop while we have not reached the last line
        try_count += 1
        i2 = dict(i) #get a new copy of dict every iteration

        #change a jmp to nop
        change_nop_jmp = list_of_nop_jmp.pop()
        log(f'changing line %d and value %s' % ( change_nop_jmp, i2[change_nop_jmp] )  )
        old_vals = i2[change_nop_jmp].split(" ")
        if old_vals[0] == 'jmp':
            i2[change_nop_jmp] = i2[change_nop_jmp].replace('jmp','nop')
        elif old_vals[0] == 'nop':
            i2[change_nop_jmp] = i2[change_nop_jmp].replace('nop','jmp')
        else: 
            print('error replacing nop_jmp')

        chk = check_loop(i2)
        if chk[1] >= len(i) - 1:  #stop when last line reached
            break 
    
    return chk, try_count

    

LOGGING = 0
l = open_file('D:/GIT/AOC2020-1/day08/input.txt', sep='\n')
i = dict(enumerate(l))

#part 1
res = check_loop(i)
print(f'loop starts at linenum %d with accumulator %d' % (res[1], res[0]) )

#part 2. only change one(!) jmp to nop
#DONE: optimalisatie: alleen de nop/jmp aanpassen die in de initiele run zitten. (het gaat om slechts 1 regel die we moeten aanpassen)
chk, try_count = change_loop(i, res)
print(f'last acc = %d after %d tries' % (chk[0], try_count) )

# timeit
print(timefunc(10, change_loop, i, res))