# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftP = "([{"
        rightP = ")]}"

        stack = []
        for char in s:
            if char in leftP:
                stack.append(char)
            elif char in rightP:
                if stack == []:
                    return False
                item = stack.pop()
                if char == "]" and item != "[":
                    return False
                elif char == ")" and item != "(":
                    return False
                elif char == "}" and item != "{":
                    return False
        return stack == []
