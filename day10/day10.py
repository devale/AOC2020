import os
import re
import timeit
from collections import defaultdict

# ideas
# part 1: get numbers in sorted list, zip together with one position difference, subtract, and list.count(1) * list.count(3) 
# part 2: if there are multiple options (within 3 jolts), that splits it into a power. number of splits n results in options 2**n
# loop through the list, for each position, count the number of options within 3 jolts distance. 


def log(*args):
    if LOGGING:
        for i in args:
            print( str(i) )

def timefunc(iter, function, *args):
    def wrap():
        function(*args)
    t = timeit.Timer(wrap)
    return t.timeit(iter) / iter #average

def prep_d(d):
    d.extend([0, max(d) + 3]) #extend jolts of outlet (0) and device_adapter (+3)
    d.sort() #sort list
    return d

def solve1(d):
    #returns the number of 1 jolt differences * number of 3-jolt differences
    #zip two lists together, shifted one position
    diff = [elem2-elem1 for elem1, elem2 in zip(d, d[1:])]
    return diff.count(1) * diff.count(3)

def count_combinations(d):
    '''returns the number of combinations that can be made connecting a list of devices that have multiple options'''
    #per position, splits is the number of options between 1 and 3 jolts
    #log(d)
    d_len = len(d)
    combinations = defaultdict(int)
    combinations[0] = 1

    for p in range(0,d_len - 2):#for each val, second to last value has always 1 option.
        log(f'check pos {p} and value {d[p]}')
        n = 1
        while d[p+n] - d[p] <=3: #count options until 3 jolts
            log(f'{p} + {n} and d[p+n] = {d[p+n]}')
            combinations[p+n] += combinations[p] #adding up the sum of all previous combinations
            n+=1
        log(f'for value {d[p]} there are {n-1} options. combinations = {combinations}')
    return combinations[d_len-1] #last item has total of combinations


LOGGING = 0

f_loc = 'D:/GIT/AOC2020-1/day10/input.txt'
#set = {}, list = [], generator = ()
data = [int(line) for line in open(f_loc, 'r').read().rstrip().split("\n")] #or read().splitlines() # = list(map(int, open('input.txt', 'r').readlines()))
#i = dict(enumerate(data))
d = prep_d(data)

#part 1: factorize the number of jolt steps of 1 and 3. 
print(f'part 1: the sum of the count of diffs 1 and diffs 3 = {solve1(d)}')
# test: 220!
# real: 2244

#part 2: how many combinations can be made with the adapters to connect the charging outlet to your device? 
print(f'part 2: count of paths = {count_combinations(d)}')
# test: 19208!
# test2: 8 combinations!
# real: 3947645370368

# timeit
print(f'timeit: {timefunc(10, count_combinations, d)}' )  
#print(f'timeit: {timefunc(10, solve2_2, d)}' )          
# part 1 using list comprehension:  0.000110
# part 1 using forloop:             0.000068
# part 2:                           0.00017
