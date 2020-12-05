# AOC2020
Advent of Code - 2020

https://adventofcode.com/2020


started a bit late (20201204). still, nice project to learn & improve some coding :) 

## day 1
used some nested list comprehensions to get the result.
wouldve been better to use some itertools and/or set logic for better performance and less code. 

## day 2
for cleanup and splitting, used some replacements to spaces and split on spaces. if one of those characters would be part of a password, that would be an issue. 
could be improved with a regex.

for the logic, i used a for loop. that could be improved by some set-based approach, or list-comprehension.
example from sgraaf, list comprehension and sum :
sum([(password[low-1] == letter) ^ (password[high-1] == letter) for low, high, letter, password in l])  # uses bitwise XOR

## day 3
