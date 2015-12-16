class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        rest = gas[0] - cost[0]
        minRest = rest
        index = 0
        for i in range(1, len(gas)):
            rest += gas[i] - cost[i]
            if rest < minRest:
                minRest = rest
                index = i
        if rest >= 0:
            return (index + 1) % len(gas)
        else:
            return -1
