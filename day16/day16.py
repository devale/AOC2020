import os
import timeit
import re
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

def solve1(d):
    
    #split into datasets
    line_your_ticket = d.index('your ticket:')
    d_rules = d[:line_your_ticket]
    d_your_ticket = d[line_your_ticket+1]
    d_nearby_tickets = d[line_your_ticket+4:]
    
    #get rules
    rules_pat = re.compile('(\d+-\d+)')
    rules_ranges = []
    for r in d_rules:
        res = re.findall(rules_pat, r)
        rules_ranges.extend(res)

    log(f'rules_ranges: {rules_ranges}')

    #put all valid numbers into set
    valid = set()
    for r in rules_ranges:
        rmin, rmax = [int(s) for s in r.split('-')]
        for val in range(rmin, rmax+1):
            valid.add(val)
    log(f'{valid}')
    
    #flatten list of all values
    all_values = [int(v) for v in d_your_ticket.split(',')] + [int(val) for sublist in d_nearby_tickets for val in sublist.split(',')]
    log(f'all values: {all_values}')

    #validate
    error_rate = sum([x for x in all_values if x not in valid])
    return error_rate

def solve2(d):
    #discard invalid tickets
    #split into datasets
    line_your_ticket = d.index('your ticket:')
    d_rules = d[:line_your_ticket-1]
    d_your_ticket = d[line_your_ticket+1]
    d_nearby_tickets = d[line_your_ticket+4:]
    
    #get rules
    rules_pat = re.compile('(\d+-\d+)')
    rules_ranges = []
    for r in d_rules:
        res = re.findall(rules_pat, r)
        rules_ranges.extend(res)

    #put all valid numbers into set
    valid = set()
    for r in rules_ranges:
        rmin, rmax = [int(s) for s in r.split('-')]
        for val in range(rmin, rmax+1):
            valid.add(val)
    log(f'{valid}')


    #remove invalid tickets
    valid_tickets = []
    for ticket in d_nearby_tickets:
        all_valid = True
        for val in ticket.split(','):
            if int(val) not in valid:
                all_valid = False
                break
        if all_valid:
            valid_tickets.append( [int(v) for v in ticket.split(',')] )
    log(f'valid tickets: {valid_tickets}')

    #get rules as dict
    pat_name = re.compile('^(.+):')
    pat_ranges = re.compile('(\d+)')
    
    rules = {re.findall(pat_name,line)[0]:
    [
        range(int(re.findall(pat_ranges, line)[0]), int(re.findall(pat_ranges, line)[1])+1) #including ranges 
    ,   range(int(re.findall(pat_ranges, line)[2]), int(re.findall(pat_ranges, line)[3])+1) #including ranges
     ]
        for line in d_rules}
    log(f'rules: {rules}')
    
    #for each rule, generate possible positions. len rules and len ticket should be the same, as each val belongs at one rule/position.
    valid_positions = {}
    for k,v in rules.items(): #each rule
        valid_positions[k] = []
        position_count = len(valid_tickets[0])
        #log(f'going to check rule {k} with value {v} on {position_count} positions')
        for i in range(position_count): #each position
            valid_pos = True            
            #log(f'checking position {i}')
            for t in valid_tickets:
                #log(f'checking ticket {t}')
                if not valid_pos: 
                    #log(f'breaking ticket')
                    break
                if t[i] not in v[0] and t[i] not in v[1]: #two ranges
                    log(f'val {val} not in {v[0]} or {v[1]}')
                    valid_pos = False
                    break
                #log(f'val {val} in {v[0]} or {v[1]}. continue next val')
                    
                #break
            if not valid_pos:
                continue
            else: #  valid_pos:
                valid_positions[k].append(i)
                #log(f'valid position added: {k}:{i}')
    
    

    #for possible positions, order them by length of options...
    positions =  sorted(valid_positions.items(), key=lambda k: len(k[1]) ) 
    log(f'positions: {positions}')

    #...and remove a fixed position from the other options. Like solving a sudoku.
    final_positions = {}
    given_positions = set()
    for k, v in positions: 
        for p in v:
            if p not in given_positions:
                given_positions.add(p)
                final_positions[k] = p
    log(f'final positions: {final_positions}')

    #return the multiplication of values on my ticket on the positions that start with departure
    multiplication = 1
    my_ticket = [int(t) for t in d_your_ticket.split(',')]
    for k, p in final_positions.items():
        if k.startswith('departure'):
            log(f'{k} has position {p}')
            multiplication *= my_ticket[p]
    return multiplication


LOGGING =  0

f_loc = 'D:/GIT/AOC2020-1/day16/input.txt'
#set = {}, list = [], generator = ()
#data = [int(x)  for line in open(f_loc, 'r').read().rstrip().split("\n") for x in line.split(',') if x != 'x' ] #or read().splitlines() 
#data = [x for line in open(f_loc, 'r').read().rstrip().split("\n") for x in line.split(',') ]
data = [line for line in open(f_loc, 'r').read().rstrip().split("\n") ]
#data = list(map(char_to_int, open(f_loc, 'r').readlines()))
#i = dict(enumerate(data))

print('\n---- part 1 ----') 
print(f'sum of all invalid numbers for any of the validation rules: {solve1(data)}') # 26869
 
print('\n---- part 2 ----')
print(f'multiplication of all values of fields that start with departure: {solve2(data)}')  #855275529001

# timeit
#print(f'timeit: {timefunc(10, solve2, data)}' )          
# part 1: 0.008s
# part 2: 0.049s