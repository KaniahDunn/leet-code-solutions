# 442. Find All Duplicates in an Array
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = []
        for elem in nums:
            num = abs(elem)
            if nums[num-1] < 0:
                count.append(num)
            else:
                nums[num-1] *= -1 
        return count