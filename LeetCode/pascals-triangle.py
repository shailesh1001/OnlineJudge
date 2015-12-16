class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = [1]
        triangle = []
        if numRows >= 1:
            triangle.append(l[:])
        for n in range(2, numRows + 1):
            l.append(1)
            for i in range(n - 2, 0, -1):
                l[i] += l[i - 1]
            triangle.append(l[:])
        return triangle
