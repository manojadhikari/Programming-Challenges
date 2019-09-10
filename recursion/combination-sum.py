'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def sum_helper(cur_res, start, target):
            if  target == 0:
                result.append(cur_res.copy())
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                cur_res.append(candidates[i])
                sum_helper(cur_res, i, target - candidates[i])
                cur_res.pop()


        result = []
        candidates.sort()
        sum_helper([], 0, target)
        return result
