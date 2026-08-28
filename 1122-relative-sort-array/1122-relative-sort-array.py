class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = [0] * 1001

        for num in arr1:
            count[num] += 1

        result = []

        for num in arr2:
            while count[num] > 0:
                result.append(num)
                count[num] -= 1

        for num in range(1001):
            while count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result