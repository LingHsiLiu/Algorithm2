# 42. Maximum Subarray II
# Given an array of integers, find two non-overlapping subarrays which have the largest sum.
# The number in each subarray should be contiguous.
# Return the largest sum.

# Example
# For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.

# Challenge
# Can you do it in time complexity O(n) ?

# Notice
# The subarray should contain at least one number

class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        n = len(nums)
        a = nums[:]
        aa = nums[:]
        for i in range(1, n):
            a[i] = max(nums[i], a[i-1] + nums[i])
            # print(a[i])
            aa[i] = max(a[i], aa[i-1])
            # print(aa[i])
        b = nums[:]
        bb = nums[:]
        for i in range(n-2, -1, -1):
            b[i] = max(b[i+1] + nums[i], nums[i])
            bb[i] = max(b[i], bb[i+1])
        mx = -33333
        
        # print(a)
        # print(aa)
        # print(bb)
        # print(b)
        
        for i in range(n-1):
            mx = max(aa[i]+b[i+1], mx)
        
        return mx
