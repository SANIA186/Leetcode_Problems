class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n):
            current = nums[i % n]

            while stack and nums[stack[-1]] < current:
                index = stack.pop()
                result[index] = current

            if i < n:
                stack.append(i)

        return result