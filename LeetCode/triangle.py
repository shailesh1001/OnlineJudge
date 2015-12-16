class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        minis = [0] * len(triangle)
        minis[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            minis[i] = triangle[i][i] + minis[i-1]
            for j in range(i-1, 0, -1):
                minis[j] = triangle[i][j] + min(minis[j], minis[j-1])
            minis[0] = triangle[i][0] + minis[0]
        return min(minis)
