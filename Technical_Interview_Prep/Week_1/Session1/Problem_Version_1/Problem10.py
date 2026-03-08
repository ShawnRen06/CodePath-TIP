'''
Problem 10: Last Item
Write a function get_last() that takes in a list as a parameter and returns the last item in the list. 
Return None if the list is empty.

def get_last(lst):
    pass
Example Input: [3,1,6,7,5]
Example Output: 5


'''
def get_last(lst):
    if len(lst) > 1:
        last = len(lst) - 1
        return lst[last]
    else:
        return None
    
print(get_last([]))