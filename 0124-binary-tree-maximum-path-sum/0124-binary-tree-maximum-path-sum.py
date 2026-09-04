class Solution:
    def maxPathSum(self, root):
        self.answer = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Path passing through the current node
            current = node.val + left + right

            self.answer = max(self.answer, current)

            # Return the best one-sided path to parent
            return node.val + max(left, right)

        dfs(root)
        return self.answer