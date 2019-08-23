'''
Find the sum of contiguous subarray within an array of numbers (both positive and negative) which has the largest sum.

Return an integer representing the largest sum

Test:
Input: [-2, 4, -1, -2, 1, 5, -2, -15, 2, 3]
Output: 7
'''

def largetst_sum(input_list):
    end = 0

    max_sum = -float('inf') 
    cur_sum = 0
    while end < len(input_list):

        cur_sum += input_list[end]
        if cur_sum > max_sum:
            max_sum = cur_sum
        
        if cur_sum < 0:
            cur_sum = 0
        
        end += 1

    return max_sum


result = largetst_sum([-2, 4, -1, -2, 1, 5, -2, -15, 2, 3])
print(result)
