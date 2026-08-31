"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        
        if not head:
            return head

        current = head

        while current:
            
            # If there is no child, simply move forward
            if not current.child:
                current = current.next
                continue

            # Save the next node
            next_node = current.next

            # Get the child list
            child = current.child

            # Connect current to child
            current.next = child
            child.prev = current

            # Remove child pointer
            current.child = None

            # Find the last node of child list
            tail = child

            while tail.next:
                tail = tail.next

            # Connect child list to original next
            tail.next = next_node

            if next_node:
                next_node.prev = tail

            # Move forward
            current = current.next

        return head