class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = "{0}".format(nums[i])
        nums.sort(lambda x, y: cmp(y + x, x + y))
        s = ""
        for i in range(0, len(nums)):
            s += nums[i]
        if s[0] == '0':
            s = "0"
        return s