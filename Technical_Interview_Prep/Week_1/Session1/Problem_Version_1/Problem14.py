'''

Problem 14: Total Sum in Range
Write a function sum_range() that returns the sum of numbers from a given start value to a given stop value (inclusive).

def sum_range(start, stop):
    pass
Example Usage: sum = sum_range(3, 9)
Example Result: sum = 42



'''

def sum_range(start,stop):
    total = 0
    for i in range(start, stop + 1):
        total += i
    return total
sum = sum_range(3,9)
print(sum)