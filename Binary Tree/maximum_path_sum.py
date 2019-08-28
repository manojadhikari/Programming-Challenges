'''
124. Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        Time: O(N)
        Space: O(H)
        """
        max_sum = [-float('inf')]
        self.maxPathSumPostOrder(root, max_sum)
        
        return max_sum[0]
    
    def maxPathSumPostOrder(self,root, max_sum):
        if root == None:
            return 0
        
        left_sum = self.maxPathSumPostOrder(root.left, max_sum)
        right_sum = self.maxPathSumPostOrder(root.right, max_sum)
        
        total_sum = max(left_sum+root.val, right_sum+root.val)
        three_sum = left_sum + right_sum + root.val
        
        max_sum[0] = max(max_sum[0], three_sum)
        
        
        if total_sum > 0:
            return total_sum
        
        return 0
    
    
    
    
        