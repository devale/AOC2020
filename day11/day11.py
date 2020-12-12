import os
import re
import timeit
import copy

# ideas
# part 1: use an 2d-array with seats. loop through seat and update accordingly by counting adjacent positions as cnt. 
# if cnt=0 then occupied (person sits), if 4+ then becomes empty (person walks away). while loop might be fastest, as it stops as soon as hitting 4.
# be aware, everything happens simultaniously, so keep a second copy (update) and switch (orginal = update) afterwards.
# if not performing, use pandas dataframes

def log(*args):
    if LOGGING:
        for i in args:
            print( str(i) )

def timefunc(iter, function, *args):
    def wrap():
        function(*args)
    t = timeit.Timer(wrap)
    return t.timeit(iter) / iter #average


def char_to_int(l):
    '''converts .=-1, L=0, #=1'''
    res = []
    for c in l:
        if c == 'L':
            res.append(0)
        elif c == '.':
            res.append(-1)
    #log(f'converting {l} to {res}')
    return res

def check_surrounding_cells(d, pos, tolerance=3):
    '''checks 8 surrounding seats (until tollerance) of position pos (x,y) and returns occupancy in next round  (True = seated, False = empty)'''
    taken = 0
    y, x = pos[0], pos[1]
    max_x = len(d[0]) - 1
    max_y = len(d) - 1
    for ydelta in range(-1,2):
        for xdelta in range(-1,2):
            x_check = x+xdelta 
            y_check = y+ydelta
            #skip when comparing itself, or out of matrix bounds
            #log(f'for yx {y} {x}, checking y:{y_check} and x:{x_check}')
            if ((xdelta == 0 and ydelta == 0 )  
                or x_check < 0 or x_check > max_x 
                or y_check < 0 or y_check > max_y): 
                #log(f'out of bounds or self')
                continue
            elif d[y_check][x_check] != 1:
                #log('not taken')
                continue
            else:
                #log(f'taken: yx-check {y_check},{x_check} has val: {d[y_check][x_check]}')
                taken += 1
                if taken > tolerance:
                    return taken
    return taken



def check_sightline_cells(d, pos, tolerance=4):
    '''count taken seats in sightlines (until tollerance) of position pos (x,y) and returns occupancy in next round  (True = seated, False = empty)'''
    taken = 0
    y, x = pos[0], pos[1]
    max_x = len(d[0]) - 1
    max_y = len(d) - 1
    for sign in [-1,1]: 
        log(f'sign: {sign}')
        for ydelta in range(1,max_y): # up then down depending on sign
            y_check = y + ydelta * sign
            log(f'verticals: for y,x:{y},{x} checking y_check:{y_check}')
            if y_check < 0 or y_check > max_y:
                log('out of bounds')
                break
            seat = d[y_check][x]
            log(f'seat: {seat}')
            if seat == -1: #nonseat, keep looking
                log('nonseat')
                continue
            elif seat == 1: # taken
                log('taken')
                taken += 1
                if taken > tolerance:
                    return taken
            log(f'empty')
            break #else empty seat, stop looking
        
        for xdelta in range(1,max_x): # left then right depending on sign
            x_check = x + xdelta * sign
            log(f'horizontals: for y,x:{y},{x}, checking x:{x_check}')
            if x_check < 0 or x_check > max_x:
                break
            seat = d[y][x_check]
            if seat == -1: #nonseat, keep looking
                continue
            elif seat == 1: # taken
                taken += 1
                if taken > tolerance:
                    return taken
            break #else empty seat, stop looking
        

        max_len = max(max_x, max_y)
        #positive diagonals
        for delta in range(1,max_len): 
            x_check = x + delta * sign
            y_check = y + delta * sign
            if (x_check < 0 or x_check > max_x
                or y_check < 0 or y_check > max_y): #out of bounds
                break
            log(f'positive diagonals: for y,x:{y},{x}, checking y,x:{y_check},{x_check}')
            if  y_check < 0 or y_check > max_y: #out of bounds
                break
            seat = d[y_check][x_check]
            log(f'seat = {seat}')
            if seat == -1:
                continue
            elif seat == 1:
                taken += 1
                if taken > tolerance:
                    return taken
            break #seat empty, stop looking. 

        #negative diagonals
        for delta in range(1,max_len): 
            x_check = x + delta * sign
            y_check = y + delta * sign * -1 #negative
            if (x_check < 0 or x_check > max_x
                or y_check < 0 or y_check > max_y): #out of bounds
                break
            log(f'negative diagonals: for y,x:{y},{x}, checking y,x:{y_check},{x_check}')
            if  y_check < 0 or y_check > max_y: #out of bounds
                break
            seat = d[y_check][x_check]
            log(f'seat = {seat}')
            if seat == -1:
                continue
            elif seat == 1:
                taken += 1
                if taken > tolerance:
                    return taken
            break #seat empty, stop looking. 

    return taken





'''
d = [ \
[1,1,0,0,0],
[0,1,0,0,0],
[0,1,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]]

print(check_surrounding_cells(d, [1,0]) ) #returns True
print(check_surrounding_cells(d, [1,2]) ) #returns False

LOGGING = 1
#part 2
d = [ \
[ 1,-1, 1,-1, 1],
[-1,-1,-1,-1,-1],
[ 1,-1, 0,-1, 1],
[-1,-1,-1,-1,-1],
[ 1, 1, 1, 1, 1]] #2 taken

#print(check_sightline_cells(d, [2,2]) ) #returns 5
#print(check_sightline_cells(d, [3,2]) ) #returns 3

'''

def update_iteration(d, tolerance=3, part=1):
    '''take a copy to loop through, for seat in seats pass it to other func check_surrounding seats. '''
    d_new = copy.deepcopy(d)
    #log(f'd_new: {d_new} ' )
    updates = 0
    for y_pos in range(len(d)):
        for x_pos in range(len(d[0])):
            val = d[y_pos][x_pos]
            if val == -1 : continue
            else:
                #log(f'checking y-x-pos {y_pos},{x_pos} for value {val}')
                if part==1:
                    cnt = check_surrounding_cells(d, (y_pos, x_pos), tolerance)
                elif part==2:
                    cnt = check_sightline_cells(d, (y_pos, x_pos), tolerance)

                if val == 0 and cnt == 0: #take seat
                    #log(f'taking seat')
                    d_new[y_pos][x_pos] = 1
                    updates += 1
                elif val == 1 and cnt > tolerance: #vacant seat
                    #log(f'leaving seat')
                    d_new[y_pos][x_pos] = 0 
                    updates += 1
                else:
                    continue
    
    for l in d_new: # print each new line
        log(f'new line: {l}')
    return d_new, updates


def solve1(d):
    '''run updates until stable'''
    iterate_cnt = 0
    updates = 1
    while updates > 0 : #while not stable + safety
        iterate_cnt += 1
        d, updates = update_iteration(d, tolerance=3, part=1)
        log(f'iteration {iterate_cnt} did {updates} updates')
    
    return sum([i.count(1) for i in d])

def solve2(d):
    '''run updates until stable'''
    iterate_cnt = 0
    updates = 1
    while updates > 0 : #while not stable + safety
        iterate_cnt += 1
        d, updates = update_iteration(d, tolerance=4, part=2)
        log(f'iteration {iterate_cnt} did {updates} updates')
    
    return sum([i.count(1) for i in d])

LOGGING = 0

f_loc = 'D:/GIT/AOC2020-1/day11/input.txt'
#set = {}, list = [], generator = ()
#data = [line for line in open(f_loc, 'r').read().rstrip().split("\n")] #or read().splitlines() 
data = list(map(char_to_int, open(f_loc, 'r').readlines()))
#list of lists (rows)
#i = dict(enumerate(data))

#part 1: run iterations until seating is stable
#log(data)
#print(f'part 1: {solve1(data)}')
# test: 37 occupied seats
# real: 2489

#part 2: how many combinations can be made with the adapters to connect the charging outlet to your device? 
#print(f'part 2: {solve2(data)}')
# test: 26 
# real: 2180

# timeit
print(f'timeit: {timefunc(3, solve2, data)}' )          
# part 1: 9.5s
# part 2: 41s