'''
Problem 12: Sum of 1 to 10
Write a function sum_ten() that returns the sum of numbers from 1 to 10.

def sum_ten():
    pass
Example Usage: output = sum_ten()
Example Result: output = 55

'''
def sum_ten():
    sum = 0
    for x in range(1,10+1):
        sum += x
    return sum
    
output = sum_ten()
print(output)