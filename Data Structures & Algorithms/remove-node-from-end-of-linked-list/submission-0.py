# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head == None):
            return None
        

        pointers = {1 : head}

        start = head

        counter = 1 
        while(start.next != None):
            cur = start.next
            start = start.next
            counter += 1
            pointers[counter] = cur
        
        remove = counter - n + 1
        print(remove)
        if(remove > 1 and remove < counter):
            pointers[remove - 1].next = pointers[remove + 1]
            pointers[remove].next = None
        elif(remove > 1):
            pointers[remove - 1].next = None
        else:
            head = head.next

        return head

        