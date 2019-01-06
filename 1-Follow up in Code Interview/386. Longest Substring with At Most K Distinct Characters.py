# 386. Longest Substring with At Most K Distinct Characters
# Given a string s, find the length of the longest substring T that contains at most k distinct characters.

# Example
# For example, Given s = "eceba", k = 3,

# T is "eceb" which its length is 4.

# Challenge
# O(n), n is the size of the string s.

class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        
        hash = {}
        n = len(s)
        j = 0
        longest = 0
        
        for i in range(n):
            while j < n and (len(hash) < k or len(hash) == k and s[j] in hash):
                hash[s[j]] = hash.get(s[j], 0) + 1
                j += 1
                print(hash)
                print("do while")
            
            # len(hash) must be smaller or equal to k after while
            # print(longest)
            print(i)
            print(j)
            longest = max(longest, j - i)
            print(longest)
            
            if s[i] in hash:
                print(s[i])
                hash[s[i]] -= 1
                if hash[s[i]] == 0:
                    del hash[s[i]]
        # print()
             
        return longest
