class Solution:

    def findRedundantConnection(self, edges):

        parent = list(range(len(edges) + 1))

        def find(i):

            if parent[i] == i:
                return i

            parent[i] = find(parent[i])
            return parent[i]

        for u, v in edges:

            root_u = find(u)
            root_v = find(v)

            # If both have the same root,
            # adding this edge creates a cycle
            if root_u == root_v:
                return [u, v]

            # Join the two components
            parent[root_u] = root_v