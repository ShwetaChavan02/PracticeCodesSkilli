# check if array is sorted
# Given an integer array nums, determine whether the array is sorted in non-decreasing order.
# An array is considered sorted if every element is less than or equal to the next element.
# Return true if the array is sorted; otherwise, return false.
# 1 <= nums.length <= 10^5 -10^9 <= nums[i] <= 10^9

def isSorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True