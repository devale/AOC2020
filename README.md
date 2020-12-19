# AOC2020
Advent of Code - 2020

https://adventofcode.com/2020


started a bit late (20201204). still, nice project to learn & improve some coding :) 

## Day 1: report repair
used some nested list comprehensions to get the result.
wouldve been better to use some itertools and/or set logic for better performance and less code. 

## Day 2: password philosophy
for cleanup and splitting, used some replacements to spaces and split on spaces. if one of those characters would be part of a password, that would be an issue. could be improved with a regex.

for the logic, i used a for loop. that could be improved by some set-based approach, or list-comprehension.
example from sgraaf, list comprehension and sum :
sum([(password[low-1] == letter) ^ (password[high-1] == letter) for low, high, letter, password in l])  # uses bitwise XOR

## Day 3: toboggan downhill
skiing was fun! first approach was to count how often a position would get hit (height / width /  steps_right). then in bed i remembered modulo. 
added logging to the initial setup files. that works good. also, improved the reading in of files to new lines are skipped.

## Day 4: passport processing
the newline fix for reading in files, created in day 3's puzzle, proved not useful for day 4...! suddenly, each 'passport' consisted of multiple lines, and items of the passport had different separators (\n or space). the validation logic turned out a bit too verbose and could have been more generic with lambda functions and a function that checks a range. 

because i could not assume that values were digits when casting to an int, i used try except logic. However, i see that others dont do that.

## Day 5: binary boarding
this proved quite an easy task. the hardest part was getting the splitting of binary seats right, which is now written per letter. maybe this can be done a bit shorter, since most of the calculation is repeating the same logic/code. 
part 2 was superfast because i already had all seatids and the logic is straightforward.

## Day 6: Custom Customs
this went well. looks like a lot of these answers do follow the same kind of structure. define a funtion that returns a count of one particular object (passport, group, list of something) and then do some kind of aggregation on that list. Maybe the idea is that we can optimize this a lot by list comprehensions, less for loops, more set based approaches.
objects: comprehensions

## Day 7: Handy Haversacks
this day was quite hard for me. I realized ealy on it should've been solved with regex and recursive functions. However, the recursive part got me a bit stuck, so i reverted to a while loop + ToDo list (check bag for children, append children to todo list, keep popping until todo list is empty).
It works, but with 100 lines of code! 
objects: recursive functions

## Day 8: Handheld Halting
the setting was really cool, combining some ligh-level coding in python on the low-level 'application instructions'. The task itself was actually not too difficult. Again I used some sort of todo.pop() structure, but as optimization limited the bruteforce method for part 2 to only those lines that were being used in part 1. Thereby only checking 17 lines instead of 135 tries. Also learned about list.index('a') method, and added some sets instead of lists here and there. 
objects: sets, list.index

## Day 9: Encoding Error
todays assignment was quite easy to find a solution. it was a good practise to use an ' in set' solution,and sort the list afterwards.
iterating over a list is faster, but comparing (is in) is faster for sets. in this case, lists were 3x faster than sets! 
objects: sets vs lists

## Day 10: Adapter Array
part 1 i quickly found the algo to solve it, and im proud to see what i've learned so far. immediately thought about zipping together the list with a shifted position, and getting the diff in a list comprehension.
part 2 was quite hard to understand at first. i thought i would be able to count splits/options and use a power function 2**splits, but after some trial and error and some hints, I found out that for each option, the number of combinations grows with the number of previous options. 
objects: collections.defaultdict

## Day 11: Seating System
part 1 taught me an important lesson. list.copy() does not make a deep copy! so nested lists are not independent, causing the new situation after one iteration to not be a parallel update of all cells. Instead, importing copy.deepcopy() makes a truly independent copy. 
part 2 is finished, but performance suffered with with many for-loops, resulting in a whopping 41s. code refactoring can be done by not checking all values in len(grid), but first create a list of possible values to check. also, part 1 and part 2 can be integrated, because looking at adjacent seats is similar to looking at sightlines, where sightlines is a multiplication of adjacency.

## Day 12: Rain Risk
good to find a bit easier day in between, as i got lagging behind a bit on the more difficult days. This day got me back into the radials vs degrees and cos/sin/tan calculations by navigating based on direct instructions (part 1) and on waypoint instructions (part 2). Good fun!

## Day 13: Shuttle Search
part 2 proved really challenging to optimize for performance. the end result was in the trillions so brute force looping was out of the question. By applying some smart skipping of values, using properties of primes, we could increment/step each number (to test) with its previous number. 

## Day 14: Docking Data
creating memory encoders that changes values or change memory locations.
learned about converting ints to binary values (format) and back (int). part 2: learned about itertools.product to generate combinations. 

## Day 15: Rambunctious Recitation
found a solution using bruteforce (per definition, as the Van Eck's number sequence does not repeat)

## Day 16: Ticket Translation
a lot of parsing was quite ok to do. The harder parts were about deducting which positions a value could be. This was similar to deductive reasoning in sudoku puzzles. If there is 1 option for one value, then remove that option from other value's possibilities! 
In part 2 i thought about saving ranges as actual range objects, as the check can be done as a simple 'if value in range() object' .







