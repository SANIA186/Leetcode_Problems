class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []

        def backtrack(i, current):
            if i == len(nums):
                result.append(current[:])
                return

            backtrack(i + 1, current)

            current.append(nums[i])
            backtrack(i + 1, current)

            current.pop()

        backtrack(0, [])

        return result