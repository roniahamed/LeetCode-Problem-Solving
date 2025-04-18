# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        temp = head
        ln = 0
        while first:
            ln += 1
            first = first.next
        if ln < n:
            return False
        
        if ln == n:
            return head.next

        while ln-n-1:
            temp = temp.next
            ln -= 1
        temp.next = temp.next.next

        return head

        