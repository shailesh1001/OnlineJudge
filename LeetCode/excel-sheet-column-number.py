class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        w = 1
        num1 = 0
        num2 = 0
        for c in s:
            num1 *= 26
            num1 += (ord(c) - ord('A'))
            num2 += w
            w *= 26
        return num1 +num2
