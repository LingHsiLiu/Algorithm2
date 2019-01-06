# 406. Minimum Size Subarray Sum
# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.

# Example
# Given the array [2,3,1,2,4,3] and s = 7, the subarray [4,3] has the minimal length under the problem constraint.

# Challenge
# If you have figured out the O(nlog n) solution, try coding another solution of which the time complexity is O(n).


class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        if nums is None and len(nums) == 0:
            return -1
        n = len(nums)        
        sum = 0
        j = 0
        minLength = n + 1
        for i in range(n):
            while j < n and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                minLength = min(minLength, j-i)
            sum -= nums[i]
            
        if minLength == n + 1 :
            return -1
        return minLength
        


