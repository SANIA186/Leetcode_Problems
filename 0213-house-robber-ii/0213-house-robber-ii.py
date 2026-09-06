class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def robLine(arr):
            prev2 = 0
            prev1 = 0

            for money in arr:
                current = max(prev1, prev2 + money)

                prev2 = prev1
                prev1 = current

            return prev1

        case1 = robLine(nums[:-1])  # exclude last
        case2 = robLine(nums[1:])   # exclude first

        return max(case1, case2)