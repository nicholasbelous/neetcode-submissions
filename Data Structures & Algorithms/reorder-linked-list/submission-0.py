# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if(head == None):
            return
        
        slow, fast = head, head

        while(fast):
            fast = fast.next
            if(fast == None):
                break
            fast = fast.next
            slow = slow.next

        start = head
        while(start):
            if(start.next == slow):
                start.next = None
                break
            start = start.next


        prev, curr = None, slow

        while(curr):
            curr.next, prev, curr = prev, curr, curr.next
         # now prev is the new head of the second list


        first = head
        second = prev

        # Keep merging as long as there are nodes left in the second half
        while first and second:
            next_first = first.next
            next_second = second.next
            
            first.next = second
            
            # If first was the very last node of the first half, 
            # we don't want to overwrite second.next with None prematurely
            if next_first is None:
                break
                
            second.next = next_first
            
            first = next_first
            second = next_second




        