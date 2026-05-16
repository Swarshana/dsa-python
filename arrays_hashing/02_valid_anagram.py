# Problem: Valid Anagram
# Link: https://neetcode.io/problems/is-anagram
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)  # since only 26 lowercase letters (constant space)

# Approach: HashMap Frequency Count
# Count character frequencies in both strings and compare the dictionaries.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT