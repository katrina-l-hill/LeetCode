# 100. Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:

#      1        1
#     / \      / \
#    2   3    2   3

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:

#      1        1
#     /        /
#    2        2

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:

#      1        1
#     / \      / \
#    2   1    1   2

# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # Base case
        # If both trees are null, they are the same, so return True
        if not p and not q:
            return True

        # If one tree is null and the other has a node, or if the values of the trees are not the same, return False
        if not p or not q or p.val != q.val:
            return False

        # Check if there is a root, and check the value of the root. If the value is the same in both trees, return True, otherwise return False
        return self.isSameTree(p.left, q.left) and (self.isSameTree(p.right, q.right))
