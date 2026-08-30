# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
       

        # Edge cases
        if not head or not head.next:
            return head

        # Odd pointer starts at first node
        odd = head

        # Even pointer starts at second node
        even = head.next

        # Save the beginning of even list
        evenHead = even

        # Rearrange the nodes
        while even and even.next:

            # Connect odd node to next odd node
            odd.next = even.next
            odd = odd.next

            # Connect even node to next even node
            even.next = odd.next
            even = even.next

        # Attach even list after odd list
        odd.next = evenHead

        return head 