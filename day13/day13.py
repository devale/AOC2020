import os
import timeit
import numpy as np
from itertools import count

# ideas
# part1: for each bus, generate multiples until above my arrival time at the bus stop. then get the remainder in minutes. 
# part2: enumerate as x also counts as a minute position. 
# chinese remainder problem video: https://www.youtube.com/watch?v=zIFehsBHB8o

def log(*args):
    if LOGGING:
        for i in args:
            print( str(i) )

def timefunc(iter, function, *args):
    def wrap():
        function(*args)
    t = timeit.Timer(wrap)
    return t.timeit(iter) / iter #average

def solve1(d):
    arrival = d[0]
    log(f'arrival: {arrival}')
    sched = d[1:]
    log(f'{sched}')
    waits = {}
    for bus in sched:
        t = bus
        while t <= arrival:
            t+=bus
        wait = t - arrival
        waits[bus] = wait
        log(f'adding bus {bus} with waittime {wait}')
    earliest_bus = min(waits.keys(), key=(lambda k: waits[k])) #returns lowest value in dict
    return  earliest_bus * waits[earliest_bus] #returns lowest value in dict

def solve2(d):
    sched = d[1:]

    #clean up: add indices, remove x, sort
    sched_cl = sorted([(i,int(b)) for i, b in enumerate(sched) if b!='x'] , reverse=True)
    log(sched_cl)

    t, step = 0, 1
    for index, bus in sched_cl:
        for c in count(t, step):
            log(f'c = {c}, index={index}, step={step}, bus={bus}')
            if (c + index) % bus == 0:
                t, step = c, step * bus
                log(f'step = {step}')
                break
    return t

    
LOGGING =  0

f_loc = 'D:/GIT/AOC2020-1/day13/input.txt'
#set = {}, list = [], generator = ()
data = [int(x)  for line in open(f_loc, 'r').read().rstrip().split("\n") for x in line.split(',') if x != 'x' ] #or read().splitlines() 
data2 = [x for line in open(f_loc, 'r').read().rstrip().split("\n") for x in line.split(',') ]
#data = list(map(char_to_int, open(f_loc, 'r').readlines()))
#i = dict(enumerate(data))

#part 1: follow nav instructions and see which position is landed.
print('\n---- part 1 ----')
#print(f'lowest waittime * busID: {solve1(data)}') # 1909372

#part 2: nav instructions are about moving a waypoint in a relative position around the ship. F means move towards waypoint.
print('\n---- part 2 ----')
print(f': {solve2(data2)}') 


# timeit
#print(f'timeit: {timefunc(10, solve2, data)}' )          
# part 1: 
# part 2: