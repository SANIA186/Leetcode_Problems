class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum = 0
        total_sum= sum(nums)
        for i in range(len(nums)):
             if leftsum  == total_sum - leftsum - nums[i]:
                return i
             leftsum += nums[i]

        return -1


            