class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hamming = 0
        while n != 0:
            hamming += 1
            n &= (n - 1)
        return hamming
