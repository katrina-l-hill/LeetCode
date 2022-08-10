# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
#     1-->2-->4
#     1-->3-->4

# 1-->1-->2-->3-->4-->4

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    # Constructor to create Node class that has properties for the value stored in the Node, and a pointer to the next Node
    def __init__(self, value, next=None):
        self.value = value  # Assign value
        self.next = next
        self.next = None  # Initialize next as Null


class Solution:
    def mergeTwoLists(self, list1):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        # Create a new linked list with dummy as the head.
        # 0 is just a value for the index position
        dummy = ListNode(0)
        head = dummy

        # While loop if neither list has reached the end
        while list1 != None and list2 != None:
            # Compare the pointers of each list to see which one is lower
            if list1.val < list2.val:
                # The dummy node points to the next node
                # In this case, it's for list1
                dummy.next = list1
                # move the pointer in list1 forward to the next node
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            # Reassign the dummy pointer to keep up with the next nodes
            dummy = dummy.next
        # If statement for when each list reaches the end
        if list1 == None:
            # Need to add the rest of the nodes from list2 if list1 is exhausted
            # Each node has a reference to it's next node
            dummy.next = list2
        else:
            dummy.next = list1
        # Return the value after None
        return head.next
