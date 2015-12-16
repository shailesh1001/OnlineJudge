# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        root2 = None
        if root:
            root2 = TreeNode(root.val)
            self.invertClone(root, root2)
        return root2
        
    def invertClone(self, root1, root2):
        if root1.left:
            root2.right = TreeNode(root1.left.val)
            self.invertClone(root1.left, root2.right)
        if root1.right:
            root2.left = TreeNode(root1.right.val)
            self.invertClone(root1.right, root2.left)
