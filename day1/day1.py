from day1funcs import *

# Part 1
with open('day1input.txt') as f:
    content = f.readlines()

nums = []

numstrs = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0
for line in content:
    sum += find_number(line)

print(sum)