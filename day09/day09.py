import os
import re
import timeit

# ideas
# part 1: iterate through the nums, taking a set of the previous x numbers. then the diff between num and setitem, should be in the set.
# part 2: take a selection, keep increasing the end of the selection while the sum its lower. if larger than the number we're looking for, start over with an increased start position.
# if its equal, solution found and return the set.

def log(*args):
    if LOGGING:
        for i in args:
            print( str(i) )

def timefunc(iter, function, *args):
    def wrap():
        function(*args)
    t = timeit.Timer(wrap)
    return t.timeit(iter) / iter #average

def find_invalid_num(d, prenums=25):
    
    for i in range(prenums,len(d)): # for every num after the preamble
        found = False
        log(d)
        num = d[i]
        log(num)
        s_25 = set(d[i-prenums:i]) #set of previous numbers
        log(f'set_25: %s' % (s_25) )
        
        #check if a combination can be made
        for j in s_25:
            log(f'diff between num %d and setitem %d = %d' % (num, j, num-j) )
            if num-j in s_25:
                found = True
                break
        if found:
            continue
        else: 
            return num

def find_contiguous_list(d, num):
    sel_start = 0
    
    #while sum of selection < num, take the next item.keep increasing pos_end until sum > num
    while sel_start < len(d):
        sel_end = sel_start + 1
        total = 0
        while total < num:
            #s = set(d[sel_start:sel_end]) #set
            s = d[sel_start:sel_end] #list
            total = sum(s)
            if total == num:
                #return sorted(list(s)) #set
                return sorted(s) #list
            else:
                sel_end += 1 
        sel_start += 1
    return -1

f_loc = 'D:/GIT/AOC2020-1/day09/input.txt'
#set = {}, list = [], generator = ()
data = [int(line) for line in open(f_loc, mode='r').read().split("\n")] #or read().splitlines()
LOGGING = 0
#i = dict(enumerate(data))

#part 1: find the first number that cannot be created from previous 25 numbers
print(f'part 1: the invalid number that cannot be created: %d'  % find_invalid_num(data, prenums=25))
#1212510616

#part 2: find a list of contiguous numbers that sum up to the number found in part 1:  1212510616
# then sum the lowest and highest number.
res = find_contiguous_list(data, 1212510616)
print(f'the sum of first and last number of contiguous list of nums that sum to answer of part 1: %d' % (res[0] + res[-1]) )

# timeit
#print(timefunc(10, find_contiguous_list, data, 1212510616))
# using sets: average of 1.09 seconds
# using lists: average of 0.3475 seconds
# using version from evanraalte: 0.0068 seconds


'''
#better by evanraalte using a generator. 
def find_contiguous_list2(d, num):
    d = [a for a in d if a < num ]
    val = False
    n = 2
    while not val: #
        val = next((min(d[i:i+n]) + max(d[i:i+n]) for i in range(0,len(d)-n) if sum(d[i:i+n]) == num),False)
        n += 1
    return val
'''
