class Solution:
    def rob(self, root):
        
        def dfs(node):
            if not node:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            # Rob current node
            rob = node.val + left[1] + right[1]

            # Don't rob current node
            skip = max(left[0], left[1]) + max(right[0], right[1])

            return [rob, skip]

        rob, skip = dfs(root)

        return max(rob, skip)