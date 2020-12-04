#import re #regex
import os


os.chdir(r'D:/GIT/AOC2020-1')

with open('day02/input.txt', mode='r') as f:
    l = f.readlines()# .split('\n')

def validate_input(l):
    print(type(l))
    print(len(l))
    print(l[:5])

def strsplit(line):
    #replace separators with space, then split on space.
    l1 = line.rstrip().replace("-"," ").replace(":"," ").split(" ")
    return l1 

#part1
def validate_pw(line):
    l = strsplit(line)
    minimum =   int(l[0])
    maximum =   int(l[1])
    char =      l[2]
    pw = l[-1]

    cnt = pw.count(char)

    if minimum <= cnt <= maximum:
        valid = 1
    else: 
        valid = 0
    return valid

#part2
def validate2_pw(line):
    l = strsplit(line)
    pos1 =   int(l[0])
    pos2 =   int(l[1])
    char =      l[2]
    pw = l[-1]

    cnt = 0 
    cnt += pw[pos1-1] == char
    cnt += pw[pos2-1] == char
    if cnt == 1:
        valid = 1
    else: 
        valid = 0
    return valid

#validate_input(l)

#part1
cnt1 = 0
for line in l:
    cnt1 = cnt1 + validate_pw(line)
print(f'the number of valid cases for part 1 = %d' % cnt1)

#part2
cnt2 = 0
for line in l:
    cnt2 = cnt2 + validate2_pw(line)
print(f'the number of valid cases for part 2 = %d' % cnt2)