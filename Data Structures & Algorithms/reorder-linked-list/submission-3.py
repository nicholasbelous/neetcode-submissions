# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if(head == None or head.next == None):
            return None


        my_nums = [head]

        while head.next != None:
            head = head.next
            my_nums.append(head)

        left, right = 0, len(my_nums) -1

        while left < right:
            my_nums[left].next = my_nums[right]
            if(left + 1 < right):
                my_nums[right].next = my_nums[left + 1]
            left += 1
            right -= 1

        my_nums[left].next = None

        return None

