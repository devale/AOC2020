import os
import math #for radians
import timeit

def log(*args):
    if LOGGING:
        for i in args:
            print( str(i) )

def timefunc(iter, function, *args):
    def wrap():
        function(*args)
    t = timeit.Timer(wrap)
    return t.timeit(iter) / iter #average


def reorient(orientation,dir,deg):
    if dir == 'R':
        deg *= -1
    orientation += deg
    return orientation % 360 

def degrees_to_pos(orientation, num):
    angle = math.radians(orientation)
    xd = math.sin(angle) * num
    yd = math.cos(angle) * num   
    return round(xd), round(yd)

def pos_to_degrees(xw, yw):
    return round(math.degrees(math.atan2(yw, xw)) )

def rotate(x,y,degrees):
    rad = (degrees/90) * (math.pi/2)
    return (
        round(x * math.cos(rad) - y * math.sin(rad)),
        round(x * math.sin(rad) + y * math.cos(rad))
    )

def solve1(instr):
    x, y = 0, 0
    orientation = 90
    for i in instr:
        com = i[:1]
        num = int(i[1:])
        if com == 'E':   x+=num
        elif com == 'N': y+=num
        elif com == 'S': y-=num
        elif com == 'W': x-=num
        elif com in ['R','L']:
            orientation = reorient(orientation,com,-num)
            log(f'{i} => new orientation: {orientation}')
        elif com =='F':
            xd, yd = degrees_to_pos(orientation, num )
            x += xd
            y += yd
        log(f'{i} => new position: {x},{y}')
    return abs(x)+abs(y)

def solve2(instr):
    '''convert the waypoint position to orientation, when moving F then update x,y'''
    x,y = 0,0
    xw, yw = 10, 1 #waypoint start
    
    #turn relative coordination point into degrees
    for i in instr:
        log(f'---{i}---')
        com = i[:1]
        num = int(i[1:])
        if   com == 'E': xw+=num
        elif com == 'N': yw+=num
        elif com == 'S': yw-=num
        elif com == 'W': xw-=num
        elif com in ['R','L']:
            '''
            vector = math.sqrt(xw**2 + yw**2) #length of the current waypoint
            log(f' vector= {vector}')
            orientation = pos_to_degrees(xw,yw) #current degrees of waypoint 
            log(f' new orientation = {orientation}')
            orientation = reorient(orientation,com,num) #updated degrees
            yw, xw = degrees_to_pos(orientation, vector) #get position of waypoint using degrees and vector
            log(f'new orientation {orientation} and waypoint {xw},{yw}')
            '''
            num_signed = num
            if com == 'R':
                num_signed *= -1
            xw, yw = rotate(xw, yw, num_signed)         

        elif com =='F':
            x += xw * num
            y += yw * num
            
        log(f'{i} => new position: {x},{y}, waypoint {xw},{yw}')
    return abs(x)+abs(y)
    
LOGGING =  0

f_loc = 'D:/GIT/AOC2020-1/day12/input.txt'
#set = {}, list = [], generator = ()
data = [line for line in open(f_loc, 'r').read().rstrip().split("\n")] #or read().splitlines() 
#data = list(map(char_to_int, open(f_loc, 'r').readlines()))
#list of lists (rows)
#i = dict(enumerate(data))

#part 1: follow nav instructions and see which position is landed.
print('\n---- part 1 ----')
print(f'manhatten distance after following direct instructions: {solve1(data)}') # 1177

#part 2: nav instructions are about moving a waypoint in a relative position around the ship. F means move towards waypoint.
print('\n---- part 2 ----')
print(f'manhatten distance after changing waypoints and following forward instructions: {solve2(data)}') 
# 29320 too low. 
# 47717 . swapped L negative and R positive angle.
# 46530. 

# timeit
#print(f'timeit: {timefunc(10, solve2, data)}' )          
# part 1: 0.0051s
# part 2: 0.0084s
