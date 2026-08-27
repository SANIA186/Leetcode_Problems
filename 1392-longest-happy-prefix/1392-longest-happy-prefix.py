class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)

        lps = [0] * n

        prefix_len = 0
        i = 1

        while i < n:

            if s[i] == s[prefix_len]:
                prefix_len += 1
                lps[i] = prefix_len
                i += 1

            elif prefix_len > 0:
                prefix_len = lps[prefix_len - 1]

            else:
                lps[i] = 0
                i += 1

        happy_prefix_len = lps[n - 1]

        return s[:happy_prefix_len] 