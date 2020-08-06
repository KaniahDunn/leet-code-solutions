# 342. Power of Four
# Easy
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if (num == 0):
            return False
        while (num != 1):
            if (num % 4 != 0): 
                return False
            num = num
        return True