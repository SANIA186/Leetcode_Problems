class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []

        candidates.sort()

        def backtrack(start, current, total):

            # Target reached
            if total == target:
                result.append(current[:])
                return

            # Target exceeded
            if total > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose
                current.append(candidates[i])

                # Explore
                backtrack(i + 1, current, total + candidates[i])

                # Undo choice
                current.pop()

        backtrack(0, [], 0)

        return result