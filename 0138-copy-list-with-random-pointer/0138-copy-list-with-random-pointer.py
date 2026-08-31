"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        

        # Empty list
        if head is None:
            return None

        # Dictionary to store:
        # original node -> copied node
        mp = {}

        def copy(node):

            # If node is None
            if node is None:
                return None

            # If node is already copied
            if node in mp:
                return mp[node]

            # Create a new node
            newNode = Node(node.val)

            # Store original -> copy
            mp[node] = newNode

            # Copy next pointer
            newNode.next = copy(node.next)

            # Copy random pointer
            newNode.random = mp.get(node.random)

            return newNode

        return copy(head)
        