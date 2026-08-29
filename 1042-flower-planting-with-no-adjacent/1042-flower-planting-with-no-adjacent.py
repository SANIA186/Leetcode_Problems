class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        

        # Create empty graph
        graph = [[] for _ in range(n)]

        # Build graph
        for a, b in paths:
            a = a - 1
            b = b - 1

            graph[a].append(b)
            graph[b].append(a)

        # 0 = no flower assigned
        ans = [0] * n

        # Color each garden
        for i in range(n):

            # Flowers used by neighboring gardens
            used = set()

            # Check neighbors
            for j in graph[i]:
                if ans[j] != 0:
                    used.add(ans[j])

            # Try flowers 1, 2, 3, 4
            for flower in range(1, 5):
                if flower not in used:
                    ans[i] = flower
                    break

        return ans