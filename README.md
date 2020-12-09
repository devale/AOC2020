# AOC2020
Advent of Code - 2020

https://adventofcode.com/2020


started a bit late (20201204). still, nice project to learn & improve some coding :) 

## day 1: report repair
used some nested list comprehensions to get the result.
wouldve been better to use some itertools and/or set logic for better performance and less code. 

## day 2: password philosophy
for cleanup and splitting, used some replacements to spaces and split on spaces. if one of those characters would be part of a password, that would be an issue. 
could be improved with a regex.

for the logic, i used a for loop. that could be improved by some set-based approach, or list-comprehension.
example from sgraaf, list comprehension and sum :
sum([(password[low-1] == letter) ^ (password[high-1] == letter) for low, high, letter, password in l])  # uses bitwise XOR

## day 3: toboggan downhill
skiing was fun! first approach was to count how often a position would get hit (height / width /  steps_right). then in bed i remembered modulo. 
added logging to the initial setup files. that works good. also, improved the reading in of files to new lines are skipped.

## day 4: passport processing
the newline fix for reading in files, created in day 3's puzzle, proved not useful for day 4...! suddenly, each 'passport' consisted of multiple lines, and items of the passport had different separators (\n or space). the validation logic turned out a bit too verbose and could have been more generic with lambda functions and a function that checks a range. 

because i could not assume that values were digits when casting to an int, i used try except logic. However, i see that others dont do that.

## day 5: binary boarding
this proved quite an easy task. the hardest part was getting the splitting of binary seats right, which is now written per letter. maybe this can be done a bit shorter, since most of the calculation is repeating the same logic/code. 
part 2 was superfast because i already had all seatids and the logic is straightforward.

## day 6: Custom Customs
this went well. looks like a lot of these answers do follow the same kind of structure. define a funtion that returns a count of one particular object (passport, group, list of something) and then do some kind of aggregation on that list. Maybe the idea is that we can optimize this a lot by list comprehensions, less for loops, more set based approaches.

## day 7: Handy Haversacks
this day was quite hard for me. I realized ealy on it should've been solved with regex and recursive functions. However, the recursive part got me a bit stuck, so i reverted to a while loop + ToDo list (check bag for children, append children to todo list, keep popping until todo list is empty).
It works, but with 100 lines of code! 

## day 8: Handheld Halting
the setting was really cool, combining some ligh-level coding in python on the low-level 'application instructions'. The task itself was actually not too difficult. Again I used some sort of todo.pop() structure, but as optimization limited the bruteforce method for part 2 to only those lines that were being used in part 1. Thereby only checking 17 lines instead of 135 tries. Also learned about list.index('a') method, and added some sets instead of lists here and there. 

## day 9: Encoding Error
todays assignment was quite easy to find a solution. it was a good practise to use an ' in set' solution,and sort the list afterwards.
iterating over a list is faster, but comparing (is in) is faster for sets. in this case, lists were 3x faster than sets! 








