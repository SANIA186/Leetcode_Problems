class Solution:
    def recoverTree(self, root):
        stack = []
        current = root
        prev = None
        first = None
        second = None

        while stack or current:

            # Go left
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            # Detect swapped nodes
            if prev and prev.val > current.val:

                if first is None:
                    first = prev

                second = current

            prev = current

            # Go right
            current = current.right

        # Swap values
        first.val, second.val = second.val, first.val