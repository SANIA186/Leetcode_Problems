from collections import Counter

class Solution:
    def reorganizeString(self, s):
        n = len(s)
        count = Counter(s)

        # If one character appears too many times
        if max(count.values()) > (n + 1) // 2:
            return ""

        result = [""] * n
        index = 0

        # Start with the most frequent character
        for ch, freq in count.most_common():

            while freq > 0:
                result[index] = ch

                # Move to next even position
                index += 2

                # If even positions are finished,
                # start from odd position
                if index >= n:
                    index = 1

                freq -= 1

        return "".join(result)