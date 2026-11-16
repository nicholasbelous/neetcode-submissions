# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)
        before = dummy
        for _ in range(left - 1):           # walk to the node just before the section
            before = before.next

        prev, curr = None, before.next
        for _ in range(right - left + 1):   # standard 206 reversal, for exactly this many nodes
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev = new head of the section; before.next = old head, now the section's tail
        before.next.next = curr             # tail connects to the rest of the list
        before.next = prev                  # the before-node connects to the new head
        return dummy.next
        

