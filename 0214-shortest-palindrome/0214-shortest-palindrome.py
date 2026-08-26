class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
      
        n = len(s)

        # Manually reverse s
        rev = ""
        i = n - 1

        while i >= 0:
            rev += s[i]
            i -= 1

        # Create combined string manually
        temp = s + "#" + rev

        # LPS array
        lps = [0] * len(temp)

        j = 0
        i = 1

        while i < len(temp):

            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]

            if temp[i] == temp[j]:
                j += 1

            lps[i] = j
            i += 1

        # Length of longest palindromic prefix
        longest = lps[len(temp) - 1]

        # Manually take required part of rev
        ans = ""
        i = 0

        while i < n - longest:
            ans += rev[i]
            i += 1

        return ans + s