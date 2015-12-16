class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = 0
        while n != 0:
            number += n // 5
            n //= 5
        return number
