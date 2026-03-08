'''
Write a function get_first() that takes in a list as a parameter and returns the first item in the list. 
Return None if the list is empty.

def get_first(lst):
    pass
Example Input: [3,1,6,7,5]
Example Output: 3

'''
def get_first(lst):
    if len(lst) > 0:
        return lst[0]
    else:
        return None
