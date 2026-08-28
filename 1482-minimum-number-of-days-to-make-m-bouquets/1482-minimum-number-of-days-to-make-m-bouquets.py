class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        

        # If we don't have enough flowers
        if m * k > len(bloomDay):
            return -1

        # Binary search range
        low = min(bloomDay)
        high = max(bloomDay)

        # Function to check if bouquets can be made
        def canMakeBouquets(day):

            bouquets = 0
            flowers = 0

            for bloom in bloomDay:

                if bloom <= day:
                    flowers += 1

                    # One bouquet is completed
                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                else:
                    # Consecutive flowers are broken
                    flowers = 0

            return bouquets >= m

        # Binary search
        while low <= high:

            mid = (low + high) // 2

            if canMakeBouquets(mid):
                # Possible, try an earlier day
                ans = mid
                high = mid - 1

            else:
                # Not possible, need more days
                low = mid + 1

        return ans
        