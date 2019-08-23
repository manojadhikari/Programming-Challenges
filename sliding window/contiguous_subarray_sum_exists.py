'''
Given an array of unsorted integers and a integer target, return true if a contiguous subarray sums up to the integer target. Otherwise, return false.
[1,4,6,21], 10 -> True
[1,4,6,21], 9 -> False

Naive Approach: Compute all subarrays. Check them one by one to see if they add to a target. O(n^3) time total
Optimal Approach: O(n) time, O(1) space Sliding Window. The solution below doesn't work for negative numbers because increasing the range of window doesn't increase the sum for negative numbers.

'''

def contiguous_sum_exists(arr1, target):
    start = 0
    end = 0
    cur_sum = 0

    while end < len(arr1):
        cur_sum += arr1[end]

        if cur_sum > target:
            cur_sum -= arr1[start]
            start += 1
        if cur_sum == target:
            return True

        end += 1

    return False
result = contiguous_sum_exists([1,4,6,21], 9)
print (result)
            
            