# Problem: Contains Duplicate
# Link: https://neetcode.io/problems/duplicate-integer
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach: hashset
# Store each number in a set. If we see a number already in the set, it's a duplicate.

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False