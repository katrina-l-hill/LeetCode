# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # comparing lengths of inputs, if not the same, then they're not an anagram
        if len(s) != len(t):
            return False

        hashmap_s = {}
        hashmap_t = {}

        # populate hashmaps with key & value pair
        for i in range(len(s)):
            # hashmap_s is the empty dict, s is the input string, and i is the loop index
            # populating the key/value pairs based on the number of times the letter appears in the string
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i], 0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i], 0)

        # check characters against each other
        for c in hashmap_s:
            # if statement to check if key/values don't match
            # if they don't match, return False (not an anagram)
            if hashmap_s[c] != hashmap_t.get(c, 0):
                return False
        return True
