# maximum element
# Given a non-empty list of integers nums, 
# find and return the maximum value in the list without using the built-in max() function.

def findMax(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max