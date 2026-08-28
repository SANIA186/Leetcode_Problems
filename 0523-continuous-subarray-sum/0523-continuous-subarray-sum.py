class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_index = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            rem = prefix % k

            if rem in remainder_index:
                if i - remainder_index[rem] >= 2:
                    return True
            else:
                remainder_index[rem] = i

        return False