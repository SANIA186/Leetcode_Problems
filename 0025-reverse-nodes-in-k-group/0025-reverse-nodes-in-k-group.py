# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        

        # Check whether we have at least k nodes
        cur = head
        group = 0

        while cur and group < k:
            cur = cur.next
            group += 1

        # If exactly k nodes are available
        if group == k:

            # Recursively reverse the remaining groups
            cur = self.reverseKGroup(cur, k)

            # Reverse the current k nodes
            while group > 0:
                tmp = head.next

                head.next = cur

                cur = head
                head = tmp

                group -= 1

            # cur is now the new head of this group
            head = cur

        # If fewer than k nodes remain,
        # return them without reversing
        return head