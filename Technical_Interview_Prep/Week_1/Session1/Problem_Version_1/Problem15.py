'''
Problem 15: Negative Numbers
Write a function print_negatives() that takes a list of integers lst and prints all negative numbers in the list.

def print_negatives(lst):
Example Usage: print_negatives([3,-2,2,1,-5])
Example Output:

-2
-5
Example Usage: print_negatives([1,2,3,4,5])
Example Output:

None

'''
def print_negatives(lst):
    count = 0
    for x in lst:
        if x < 0:
            print(x)
            count += 1
    if count == 0:
        print("None")


print_negatives([3,-2,2,1,-5])
print_negatives([1,2,3,4,5])