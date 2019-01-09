# 81. Find Median from Data Stream
# Numbers keep coming, return the median of numbers at every time a new number added.

# Example
# For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].

# For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].

# For numbers coming list: [2, 20, 100], return [2, 2, 20].

# Challenge
# Total run time in O(nlogn).

# Clarification
# What's the definition of Median?

# Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]. For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.


import heapq
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        self.minheap, self.maxheap = [], []
        medians = []
        for num in nums:
            self.add(num)
            medians.append(self.median)
        return medians
    
    @property
    def median(self):
        return -self.maxheap[0]

    def add(self, value):
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -value)
        else:
            heapq.heappush(self.minheap, value)
            
        if len(self.minheap) == 0 or len(self.maxheap) ==0:
            return

        if -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
