# fisrt duplicate element
# Given a list of integers nums, find and return the first element that appears more than once 
# (i.e. the element whose second occurrence has the smallest index).
# If no element is repeated, return -1

def first_duplicate(nums):
    visited = set()

    for num in nums:
        if num in visited:
            return num
        visited.add(num)

    return -1