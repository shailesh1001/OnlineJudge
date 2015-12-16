class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        for i in range(0, len(nums)):
            if i > farthest:
                return False
            if i + nums[i] > farthest:
                farthest = i + nums[i]
        return True
