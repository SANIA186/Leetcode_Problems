class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
      
      
        d = {0:1}

        current_sum = 0

        count = 0

        for num in nums:

            current_sum += num

            if current_sum - k in d:

                count += d[current_sum - k]

            d[current_sum] = d.get(current_sum, 0) + 1

        return count





