class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total = 0
        current =0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            current += gas[i] - cost[i]
            if current < 0 :
                start = i+1
                current = 0

        return start if total>=0 else -1
        