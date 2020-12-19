import os
import timeit
#import numpy as np
#from itertools import count

# ideas
# part1: 
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

  
LOGGING =  1

f_loc = 'D:/GIT/AOC2020-1/day14/input.txt'
#set = {}, list = [], generator = ()
#data = [int(x)  for line in open(f_loc, 'r').read().rstrip().split("\n") for x in line.split(',') if x != 'x' ] #or read().splitlines() 
#data = [x for line in open(f_loc, 'r').read().rstrip().split("\n") for x in line.split(',') ]
data = [line for line in open(f_loc, 'r').read().rstrip().split("\n") ]
#data = list(map(char_to_int, open(f_loc, 'r').readlines()))
#i = dict(enumerate(data))

print('\n---- part 1 ----')
print(f': {solve1(data)}') # 1909372

print('\n---- part 2 ----')
print(f': {solve2(data)}') 

# timeit
#print(f'timeit: {timefunc(10, solve1, data)}' )          
# part 1:
# part 2: 