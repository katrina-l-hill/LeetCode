# 226. Invert Binary Tree

# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:

#       4             4
#      / \           / \
#     2   7   -->   7   2
#    /\   /\       /\   /\
#   1  3 6  9     9  6 3  1

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:

#       2             2
#      / \           / \
#     1   3   -->   3   1

# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.left:
            root.left = self.invertTree(root.left)
        if root.right:
            root.right = self.invertTree(root.right)
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        return root
