class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = 0
        for x in nums:
            if x != val:
                nums[n] = x
                n += 1
        return n
