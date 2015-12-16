class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        negative = False
        if x < 0:
            negative = True
            x = -x;
        while x != 0:
            y = y * 10 + x % 10
            x /= 10
        if negative:
            y = -y
        if y < -(1 << 31) or y > (1 << 31) - 1:
            y = 0
        return y
        