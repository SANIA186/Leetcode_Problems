class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count = 0
        current = word

        while current in sequence:
            count += 1
            current += word

        return count
        