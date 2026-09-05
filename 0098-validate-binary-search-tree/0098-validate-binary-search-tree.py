class Solution:
    def isValidBST(self, root):
        stack = []
        prev = None
        current = root

        while stack or current:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Visit node
            current = stack.pop()

            # BST requires strictly increasing values
            if prev is not None and current.val <= prev:
                return False

            prev = current.val

            # Move to right subtree
            current = current.right

        return True