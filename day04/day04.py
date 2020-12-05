import os
import re
#import timeit

LOGGING = 0

def log(s):
    if LOGGING:
        print( str(s) )


os.chdir(r'D:/GIT/AOC2020-1')
with open('day04/input.txt', mode='r') as f:
    #f_list = f.read().splitlines() #better than readlines() as it removes \n

    #splitting must be done manually, not one passport per line.
    f_text = f.read().rstrip()    #rstrip because it ends with a new line
    f_list = f_text.split('\n\n') #split into passports.
    f_list = [re.split(' |\n', i) for i in f_list]

    #print some example lines
    #log(f'example strings splitted: %s' % f_list[:3])

def validate_pp(pp_dict):
    #checks wether all keys are in the passport

    keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] #optional:  'cid'

    valid = 0

    for item in keys:
        if item not in pp_dict.keys():
            valid = 0
            break
        else:
            valid = 1 

    return valid

# turn passport values into list of dicts 
dict_list = [dict(i.split(':') for i in pp) for pp in f_list]

#part1 - check if required fields are present
#valid_pps = sum(map(validate_pp, dict_list))
#print(f'number of valid passports %d' % valid_pps )


#part2 - validate values of fields
"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


def validate_pp_vals(pp):
    #uses regex to search for valid patterns
    #re.search('^startpatterntoend$'','string')

    patterns = {'byr':'^\d{4}$',
                'iyr': '^\d{4}$',
                'eyr':'^\d{4}$',
                'hgt':'^\d\d\d?(cm|in)$',
                'hcl':'^#[a-f0-9]{6}$',
                'ecl':'^(amb|blu|brn|gry|grn|hzl|oth)$',
                'pid':'^\d{9}$'
                }

    #returns 0 on invalidation, else 1
    for k,v in patterns.items():
        if k in pp.keys() and re.search(v, pp[k]):
            log(f'key %s and pattern valid' % k)
            if k=='byr':
                try:
                    if 1920 <= int(pp[k]) <= 2002:
                        log('valid value')
                        continue

                    else:
                        log('invalid value')
                        return 0
                except:
                    log('cannot convert')
                    return 0
            elif k=='iyr':
                try:
                    if 2010 <= int(pp[k]) <= 2020: continue
                    else: 
                        log('iyr invalid')
                        return 0
                except: 
                    log('iyr cast error')
                    return 0
            elif k=='eyr':
                try:
                    if 2020 <= int(pp[k]) <= 2030: continue
                    else: 
                        log('eyr invalid')
                        return 0
                except: 
                    log('eyr cast error')
                    return 0
            elif k=='hgt':
                try:
                    log(f'postfix: %s' % pp[k][-2:])
                    log(f'prefix: %s' % pp[k][:-2])
                    if pp[k][-2:] == 'cm' and 150 <= int(pp[k][:-2]) <= 193: continue
                    elif pp[k][-2:] == 'in' and 59 <= int(pp[k][:-2]) <= 76: continue
                    else: 
                        log('height invalid')
                        return 0
                except: 
                    log('height cast error')
                    return 0
        else:
            log(f'key/pattern invalid: %s' % k )
            return 0
    
    log('pp valid')
    return 1

valid_cnt = 0
for pp in dict_list[:]:
    log(pp)
    valid_cnt += validate_pp_vals(pp)

print(f'valid passport values: %d' % valid_cnt)
#138 too low
#146 too high --> 9-digit regex accepted 10 digits, no start-end defined.


'''
#better by maxverver:
import re
import sys

REQUIREMENTS = {
    'byr': lambda s: len(s) == 4 and 1920 <= int(s) <= 2002,
    'iyr': lambda s: len(s) == 4 and 2010 <= int(s) <= 2020,
    'eyr': lambda s: len(s) == 4 and 2020 <= int(s) <= 2030,
    'hgt': lambda s: (
        (s.endswith('cm') and 150 <= int(s[:-2]) <= 193) or
        (s.endswith('in') and 59 <= int(s[:-2]) <= 76)),
    'hcl': lambda s: re.match('^#[0-9a-f]{6}$', s) is not None,
    'ecl': lambda s: s in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda s: re.match('^[0-9]{9}$', s),
}

passports = [
    dict(entry.split(':', 1) for entry in record.split())
    for record in sys.stdin.read().split('\n\n')]

def HasAllRequiredFields(passport):
    for key in REQUIREMENTS:
        if key not in passport:
            return False
    return True

def IsValid(passport):
    for key, validator in REQUIREMENTS.items():
        value = passport.get(key)
        if value is None or not validator(value):
            return False
    return True

# Part 1
print(sum(map(HasAllRequiredFields, passports)))

# Part 2
print(sum(map(IsValid, passports)))
'''