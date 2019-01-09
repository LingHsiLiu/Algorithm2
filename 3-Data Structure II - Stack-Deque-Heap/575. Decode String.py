# 575. Decode String
# Given an expression s includes numbers, letters and brackets. Number represents the number of repetitions inside the brackets(can be a string or another expression)．Please expand expression to be a string.

# Example
# s = abc3[a] return abcaaa
# s = 3[abc] return abcabcabc
# s = 4[ac]dy, return acacacacdy
# s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz

# Challenge
# Can you do it without recursion?

class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        
        stack = []
        for c in s:
            if c !=']':
                stack.append(c)
                continue
            
            strs = []
            while stack and stack[-1] != '[':
                strs.append(stack.pop())
            # skip '['
            stack.pop()

            repeats = 0
            base = 1
            while stack and stack[-1].isdigit():
                repeats += (ord(stack.pop()) - ord('0')) * base 
                base *= 10
            stack.append(''.join(reversed(strs)) * repeats)
        
        return ''.join(stack)
