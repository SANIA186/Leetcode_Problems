class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)

        base = 26
        mod = 10**9 + 7

        # Convert characters into numbers
        nums = [ord(c) - ord('a') for c in s]

        # Check whether a duplicate substring of given length exists
        def check(length):

            if length == 0:
                return ""

            # base^(length-1) % mod
            power = pow(base, length - 1, mod)

            # Hash of first substring
            h = 0

            for i in range(length):
                h = (h * base + nums[i]) % mod

            # Store hashes we have already seen
            seen = {h}

            # Sliding window
            for i in range(length, n):

                # Remove leftmost character
                h = h - nums[i - length] * power

                # Add new character
                h = (h * base + nums[i]) % mod

                # If hash already exists
                if h in seen:

                    # Current substring
                    start = i - length + 1
                    candidate = s[start:start + length]

                    # Verify actual substring
                    for j in range(start):
                        if s[j:j + length] == candidate:
                            return candidate

                # Store current hash
                seen.add(h)

            # No duplicate substring found
            return None

        # Binary search for maximum length
        left = 1
        right = n - 1

        answer = ""

        while left <= right:

            mid = (left + right) // 2

            result = check(mid)

            if result is not None:

                # Duplicate exists
                answer = result

                # Try longer substring
                left = mid + 1

            else:

                # No duplicate
                # Try shorter substring
                right = mid - 1

        return answer
        