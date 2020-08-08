# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false
 

# Constraints:

# s consists only of printable ASCII characters.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = [char for char in s if char.isalnum()]
        l, r = 0, len(res) - 1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True