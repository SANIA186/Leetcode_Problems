class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, target, path):
            if node is None:
                return

            path.append(node.val)

            # Check if it is a leaf
            if node.left is None and node.right is None:
                if target == node.val:
                    result.append(path[:])
            else:
                dfs(node.left, target - node.val, path)
                dfs(node.right, target - node.val, path)

            path.pop()

        dfs(root, targetSum, [])
        return result