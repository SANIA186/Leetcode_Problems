class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = float('inf')

        dp = [INF] * n
        dp[src] = 0

        for _ in range(k + 1):
            temp = dp[:]

            for u, v, price in flights:
                if dp[u] != INF:
                    temp[v] = min(temp[v], dp[u] + price)

            dp = temp

        if dp[dst] == INF:
            return -1

        return dp[dst]