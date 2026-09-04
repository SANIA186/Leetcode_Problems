class Solution:
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # If k is still remaining, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        # If nothing remains
        return result if result else '0'