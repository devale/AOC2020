import os
#import re

#this is about sets to get unique chars per group, and count. 
#splitting on blank lines first to get groups, then split on rows. 


LOGGING = 1

def log(s):
    if LOGGING:
        print( str(s) )


def get_unique_chars(grp):
    return set( ''.join(grp) )
    
def get_shared_chars(grp):
    l1 = grp[0]
    for l2 in grp:
        l1 = list(set(l1) & set(l2))
    return ''.join(l1)

os.chdir(r'D:/GIT/AOC2020-1')
with open('day06/input.txt', mode='r') as f:
    #f_list = f.read().splitlines() #better than readlines() as it removes \n

    #splitting must be done manually, as groups are separated by a blank line. first on groups later on rows.
    f_text = f.read().rstrip()    #rstrip because it ends with a new line
    f_list = f_text.split('\n\n') #split into groups.
    f_list = [i.split('\n') for i in f_list] #split groups on rows to get list of lists.


sets = [get_unique_chars(grp) for grp in f_list[:] ]

#part1: count of questions to which ANYONE answered yes, per group. 
print(f'sum of group lengths that have at least once answered question: %d' % sum([len(s) for s in sets]) )

#part2: count of questions to which EVERYONE answered yes, per group
all_answered = [get_shared_chars(grp) for grp in f_list[:]]
print(f'sum of group lenghts that have all answered the same question: %d' % sum([len(s) for s in all_answered]) )

'''
better solutions include set.union and set.intersect
#better by maksverver
groups = [[set(l) for l in g.split()] for g in f.read().split('\n\n')]

print(sum(len(set.union(*g)) for g in groups))
print(sum(len(set.intersection(*g)) for g in groups))
'''