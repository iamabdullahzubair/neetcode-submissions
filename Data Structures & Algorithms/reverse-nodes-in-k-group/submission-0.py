# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            # check k nodes
            kth = groupPrev

            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            groupNext = kth.next

            # reverse group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # reconnect
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp