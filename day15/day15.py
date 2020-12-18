import os
import timeit
#import numpy as np
#from itertools import count

# ideas
# part1: keep track of counter and previous spoken number, save a dict with number and countvalue when last spoken. 
# part2: 


def log(*args):
    if LOGGING:
        for i in args:
            print( str(i) )

def timefunc(iter, function, *args):
    def wrap():
        function(*args)
    t = timeit.Timer(wrap)
    return t.timeit(iter) / iter #average

def solve1(d, limit=2020):
    mem = {}
    
    #initialize by looping through input
    counter = 1
    for num in d:    
        num_exists = num in mem
        mem[num] = counter
        counter += 1
    log(f'initial mem: {mem}')

    #iterate until counter = 2020
    while counter <= limit:
        #check
        log(f'turn: {counter}, num={num}')
        if num_exists:
            num = counter - 1 - prev_cnt #previous time minus the time before
            log(f'exists. new num is counter {counter} - previous count {prev_cnt} = {num}')
        else: 
            num = 0 
            log(f'exists: {num_exists}')

        num_exists = num in mem #check before update
        prev_cnt = mem.get(num, 0)
        
        #update
        mem[num] = counter
        log(f'mem updated: num {num} got counter {counter}')
        counter += 1


    return num
'''#better solution by maksverver
def solve2(d, limit):
    index = limit*[0]
    for i in range(1, len(d)):
        index[d[i - 1]] = i
    i = len(d)
    n = d[i - 1]
    while i < limit:
        k = index[n]
        m = 0 if k == 0 else i - k
        index[n] = i
        i += 1
        n = m
    return n
'''
LOGGING =  0

f_loc = 'D:/GIT/AOC2020-1/day15/input.txt'
#set = {}, list = [], generator = ()
#data = [int(x)  for line in open(f_loc, 'r').read().rstrip().split("\n") for x in line.split(',') if x != 'x' ] #or read().splitlines() 
#data = [x for line in open(f_loc, 'r').read().rstrip().split("\n") for x in line.split(',') ]
data = [int(line) for line in open(f_loc, 'r').read().rstrip().split("\n") ]
#data = list(map(char_to_int, open(f_loc, 'r').readlines()))
#i = dict(enumerate(data))

#part 1: follow nav instructions and see which position is landed.
print('\n---- part 1 ----')
#print(f': {solve1(data, limit=2020)}') #595

#part 2: nav instructions are about moving a waypoint in a relative position around the ship. F means move towards waypoint.
print('\n---- part 2 ----')
print(f': {solve1(data, limit=30000000)}')  #1708310


# timeit
#print(f'timeit: {timefunc(3, solve2, data, 30000000)}' )          
# part 1: 0.013
# part 2: 60-120s, using solve2 it takes 23s
