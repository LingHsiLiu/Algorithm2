# 384. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

# Example
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

# For "bbbbb" the longest substring is "b", with the length of 1.

# Challenge
# O(n) time

class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        unique_chars = set([])
        j = 0
        n = len(s)
        longest = 0
        for i in range(n):
            while j < n and s[j] not in unique_chars:
                unique_chars.add(s[j])
                j += 1
            longest = max(longest, j - i)
            unique_chars.remove(s[i])
        return longest
                
