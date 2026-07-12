# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for l in lists:
            while(l.next != None):
                heapq.heappush(minHeap, l.val)
                l = l.next
            heapq.heappush(minHeap, l.val)

        if(len(minHeap) == 0):
            return None
        head = ListNode(heapq.heappop(minHeap))
        headPointer = head

        for _ in range(len(minHeap)):
            head.next = ListNode(heapq.heappop(minHeap))
            head = head.next

        return headPointer
