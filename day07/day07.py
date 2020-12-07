import os
import re

# ideas
# regex for bagname + contents. count of content bags is not required for part 1. 
# use recursive function

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

def extract_bags(line):

    #extracts the parent bag
    pat = re.compile('^(.+) bag[s]? contain')
    res = re.findall(pat, line)
    
    #extracts children bags
    pat2 = re.compile('(\d)+\s(\D+) bag')
    res2 = re.findall(pat2, line)

    return (res, list(res2))

def dict_of_bags(l):
    d = {}
    for line in l:
        res = extract_bags(line)
        if res[0]:
            d[res[0][0]] = res[1]
    return d

def get_direct_parents(d, bag):
    parents = []
    for k,v in d.items():
        if not v:
            continue
        for item in v: 
            if bag == item[1]: #name
                log('bag %s has parent %s with factor %s' % (bag, k, item[0]) )
                parents.append(k)

    return parents

def get_all_parents(d, bag):
    to_check = get_direct_parents(d,bag)
    log('parents to check: ' + str(to_check) )
    par = []
    while to_check:
        nextitem = to_check.pop()
        #log('checking bag:' + nextitem)
        if nextitem not in par:
            par.append(nextitem)
        log('parents list:' + str(par))
        to_check.extend( get_direct_parents(d, nextitem) )

    return par

def get_all_children(d, bag):
    
    children = []
    to_check = [bag,]
    while to_check:
        log('to check: ' + str(to_check) )
        nextitem = to_check.pop()
        log(f'checking bag %s' % str(nextitem) )
        c = d.get(nextitem)
        for i in c:
            for j in range(int(i[0])): #this time we want to duplicate
                log(f'appending %s' % i[1])
                children.append(i[1])
                to_check.append(i[1])
        log(f'child list extended: %s' % str(children))
        
    return children
    
LOGGING = 0

l = open_file('D:/GIT/AOC2020-1/day07/input.txt', sep='\n')
d = dict_of_bags(l[:])
log(d)

# part 1: count parent bags
par = get_all_parents(d, 'shiny gold') 
print(f'count of (in)direct parents: %s ' % len(par) )

# part 2: count children bags with muliplier
children = get_all_children(d, 'shiny gold')
print(f'number of children = %d' % len(children)  )

