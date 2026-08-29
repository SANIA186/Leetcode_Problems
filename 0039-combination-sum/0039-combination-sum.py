class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []
        self.solve(candidates, target, 0, [], result)
        return result

    def solve(self, candidates, target, index, current, result):
        if target == 0:
            result.append(list(current))
            return

        if target < 0:
            return

        for i in range(index, len(candidates)):
            current.append(candidates[i])
            self.solve(candidates, target - candidates[i], i, current, result)
            current.pop()
