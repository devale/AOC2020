import os
import re

# ideas
# read file with a locator, so we can jump positions. seek()
# use simple string parsing since positions are fixed.

def log(s):
    if LOGGING:
        print( str(s) )

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
    lines_done = []
    acc = 0
    linenum = 0
    try_count = 0
    last_linenum = len(i) - 1 #zero index
    
    while linenum not in lines_done:
        lines_done.append(linenum)
        line = i[linenum]
        previous_linenum = linenum
        last_jmp_num = 0
        #log(line)
        instr = line[:3]
        #log(instr)
        if line[4:5] == '-': 
            sign = -1
        else: 
            sign = 1
        num = int(line[5:]) * sign
        #log(num)
        if instr == 'jmp':
            last_jmp_num = int(linenum)
            linenum += num

        else: 
            linenum += 1
        if instr == 'acc':
            acc += num

        try_count += 1
        #log(f'new linenum = %d' % linenum)

        if try_count == 10000:
            print('max tries reached')
            break
        if linenum == last_linenum:
            print('found exit!')
            break

    log(f'loop found at line %d and accumulator %d. last jump was line %d' % (linenum, acc, last_jmp_num) )
    
    return acc, linenum

LOGGING = 0
l = open_file('D:/GIT/AOC2020-1/day08/input.txt', sep='\n')
i = dict(enumerate(l))

#part 1
res = check_loop(i)
print(f'loop starts at linenum %d with accumulator %d' % (res[1], res[0]) )

#part 2. only change one(!) jmp to nop
cont = 1
try_count = 0

# get a list of all jmp instructions
jumpers = []
for k, v in i.items():
    if v[:3] == 'jmp':
        jumpers.append(k)

while cont and try_count < 1000: #loop while we have not reached the last line
    #get a new copy of dict every iteration
    i2 = dict(i)
    #change last jmp to nop
    change_jmp = jumpers.pop()
    log(f'changing line %d and value %s' % ( change_jmp, i2[change_jmp] )  )
    i2[change_jmp] = i2[change_jmp].replace('jmp','nop')

    chk = check_loop(i2)
    if chk[1] >= len(i) - 1: #stop when last line reached
        cont = 0
    try_count += 1

print(f'last acc = %d after %d tries' % (chk[0], try_count) )