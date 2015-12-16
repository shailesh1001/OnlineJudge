class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = 0
        counter = 0
        for x in nums:
            if counter != 0:
                if x == majority:
                    counter += 1
                else:
                    counter -= 1
            else:
                majority = x
                counter = 1
        return majority
