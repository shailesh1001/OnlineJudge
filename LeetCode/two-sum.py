class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i1 in range(0, len(nums)):
            for i2 in range(i1 + 1, len(nums)):
                if nums[i1] + nums[i2] == target:
                    return (i1 + 1, i2 + 1)
