class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = heights[:]

        
        for i in range(len(expected)):
            for j in range(0, len(expected) - i - 1):
                if expected[j] > expected[j + 1]:
                    expected[j], expected[j + 1] = expected[j + 1], expected[j]

        count = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count