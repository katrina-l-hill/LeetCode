# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:

#        3
#       / \
#      9  20
#         /\
#        15 7

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:

#         1
#        / \
#       2   2
#      / \
#     3   3
#    / \
#   4   4

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:

# Input: root = []
# Output: true

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root):
            # Edge case if the root has no nodes. It's still considered a balanced tree, so the return is the height of the tree along with the boolean value of True.
            if not root:
                return [True, 0]

            # This shows that from the root, a tree with null branches is balanced.
            left, right = dfs(root.left), dfs(root.right)

            # Check if the root of the subtree is balanced by taking the absolute value of the left and right heights, then compare it to 1 because it's the limited height of a balanced binary tree.
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # Balanced will return the boolean value of True or False if the tree is balanced at all.
            # This also tests the tree from the root and return a boolean value.
            # This will only be True if the left and right subtrees, and the root, are balanced.
            # Find the max values of the left and right subtrees and add them by 1. 1 comes from the root of the tree and is utilized in the function of max to return the highest number of the left and right subtrees.
            return [balanced, 1 + max(left[1], right[1])]

        # The height is returned by returning the root as a parameter and a boolean, which is shown as the index of [0].
        return dfs(root)[0]
