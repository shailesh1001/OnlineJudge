class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = "%d" % x
        indexL = 0
        indexR = len(s) - 1
        while indexL < indexR:
            if s[indexL] != s[indexR]:
                return False
            indexL += 1
            indexR -= 1
        return True
