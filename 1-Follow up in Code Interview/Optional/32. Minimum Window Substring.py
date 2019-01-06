# 32. Minimum Window Substring
# Given a string source and a string target, find the minimum window in source which will contain all the characters in target.

# Example
# For source = "ADOBECODEBANC", target = "ABC", the minimum window is "BANC"

# Challenge
# Can you do it in time complexity O(n) ?

# Clarification
# Should the characters in minimum window has the same order in target?

# Not necessary.
# Notice
# If there is no such window in source that covers all characters in target, return the emtpy string "".
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in source.
# The target string may contain duplicate characters, the minimum window should cover all characters including the duplicate characters in target.

class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        if source is None:
            return ""
            
        targetHash = self.getTargetHash(target)
        targetUniqueChars = len(targetHash)
        matchedUniqueChars = 0
        
        hash = {}
        n = len(source)
        j = 0
        minLength = n + 1
        minWindowString = ""            

        for i in range(n):
            while j < n and matchedUniqueChars < targetUniqueChars:
                if source[j] in targetHash:
                    hash[source[j]] = hash.get(source[j], 0) + 1
                    if hash[source[j]] == targetHash[source[j]]:
                        matchedUniqueChars += 1
                j += 1
            if j - i < minLength and matchedUniqueChars == targetUniqueChars:
                minLength = j - i
                minWindowString = source[i:j]
                
            if source[i] in targetHash:
                if hash[source[i]] == targetHash[source[j]]:
                    matchedUniqueChars -= 1
                hash[source[i]] -= 1 
        return minWindowString
    
    
    def getTargetHash(self, target):
        hash = {}
        for c in target:
            hash[c] = hash.get(c, 0) + 1
        return hash

