class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)

        for i in range(1, n):
            if n % i == 0:
                substring = s[:i]
                count = n // i

                if substring * count == s:
                    return True

        return False