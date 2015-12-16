class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n] = nums[i]
                n += 1
        for i in range(n, len(nums)):
            nums[i] = 0
