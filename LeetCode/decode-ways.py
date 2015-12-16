class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n1 = n2 = 0
        if len(s) > 0:
            if s[0] > '0':
                n1 = 1
                n2 = 1
            else:
                n1 = 1
                n2 = 0
            for i in range(1, len(s)):
                x = 0
                if s[i] > '0':
                    x += n2
                if s[i-1] == '1' or s[i-1] == '2' and s[i] <= '6':
                    x += n1
                n1, n2 = n2, x
        return n2
