# 1089. Duplicate Zeros

# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

# Example 1:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:

# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9


class Solution:
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None. Do not return anything, modify arr in-place instead.
        """
        # Problem Domain: fixed length array, duplicate each occcurrence of zero, shift the remaining elements to the right

        # Algorithm
        # step 1: create a temp list

        temp = []

        # step 2: iterate over input array and add items to the temp list

        for i in arr:
            # step 2.1: if statement; if item is zero, add it twice to temp list
            if i == 0:
                temp.append(i)
                temp.append(i)

            # step 2.2: else statement; add item only once
            else:
                temp.append(i)

        # step 3: copy the items in the temp list into the input array stopping before end of array
        for i in range(len(arr)):
            arr[i] = temp[i]
