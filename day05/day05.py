import os
import re
#import timeit

LOGGING = 0

def log(s):
    if LOGGING:
        print( str(s) )


os.chdir(r'D:/GIT/AOC2020-1')
with open('day05/input.txt', mode='r') as f:
    f_list = f.read().splitlines() #better than readlines() as it removes \n

def get_seat(seat):
    r_start = 0
    r_end = 127
    col_start = 0
    col_end = 7
    for char in seat:
        if char == 'B':
            r_start += 0.5 * ( r_end - r_start + 1 )
        elif char == 'F':
            r_end -=  0.5 * (r_end - r_start + 1)
        elif char == 'R':
            col_start +=  0.5 * (col_end - col_start + 1)
        elif char == 'L':
            col_end -=  0.5 * (col_end - col_start + 1)
        log(f'update: %d, %d, %d, %d' % (r_start, r_end, col_start, col_end))
    result = [-1, -1]
    if r_start == r_end and col_start == col_end:
        log(f'unique position found: row %d and seat %d' % (r_start, col_start) )
        result = [r_start, col_start]
    else:
        print('no unique seat found for %s' % seat)
        raise
    return result
    

seats = [get_seat(seat) for seat in f_list]

#part 1
seat_ids = [seat[0] * 8 + seat[1] for seat in seats]
max_seat_id = max(seat_ids)
print(f'the maximum seatid is: %d' % max_seat_id)
# 886: too high -> col was 1-8 instead of 0-7 zerobased index.


#part 2: find empty seat with seats on both sides
for i in range(0,128*8):
    if i not in seat_ids and i-1 in seat_ids and i+1 in seat_ids:
        print(i)
