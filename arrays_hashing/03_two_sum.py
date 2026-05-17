# Problem: Two Sum
# Link: https://neetcode.io/problems/two-integer-sum
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach: HashMap (One Pass)
# Store each number's index in a hashmap.
# For each number, check if (target - number) already exists in the hashmap.
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
           prevMap = {}
           for i, n in enumerate(nums):
                diff = target - n
                if diff in prevMap:
                    return [prevMap[diff],i]
                prevMap[n] = i    
