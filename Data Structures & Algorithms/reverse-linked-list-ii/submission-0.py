# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        cur = head
        nex = None

        while cur.val != left:
            prev = cur
            cur = cur.next

        end = cur

        while cur.val != right:
            prev = cur
            cur = cur.next
            nex = cur.next

            cur.next = prev

            prev = cur
            cur = nex

        end.next = cur.next
        cur.next = prev

        return cur
        

