# 363. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# Trapping Rain Water

# Example
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# Challenge
# O(n) time and O(1) memory

# O(n) time and O(n) memory is also acceptable.

class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0
            
        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        water = 0
        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, heights[left])
                water += left_max - heights[left]
                left += 1
            else:
                right_max = max(right_max, heights[right])
                water += right_max - heights[right]
                right -= 1
                    
        return water
        
        
        # if not heights:
        #     return 0
        
        # left_max = []
        # curt_max = -sys.maxsize
        # for hight in heights:
        #     curt_max = max(curt_max, hight)
        #     left_max.append(curt_max)
        
        # right_max = []
        # curt_max = -sys.maxsize
        # for hight in reversed(heights):
        #     curt_max = max(curt_max, hight)
        #     right_max.append(curt_max)
        
        # right_max = right_max[::-1]
        
        # print(left_max)
        # print(right_max)
        
        # water = 0
        # n = len(heights)
        # for i in range(n):
        #     water += (min(left_max[i], right_max[i]) - heights[i])
        #     print(water)
        # return water
