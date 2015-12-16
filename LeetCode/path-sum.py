# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        sum -= root.val
        
        if root.left or root.right:
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        else:
            return sum == 0
