class Solution:
    def lowestCommonAncestor(self, root, p, q):

        while root:

            # Both nodes are in the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left

            # Both nodes are in the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # They split here, so root is the LCA
            else:
                return root