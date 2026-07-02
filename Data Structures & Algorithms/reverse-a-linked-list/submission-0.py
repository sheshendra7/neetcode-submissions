# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        preNode ,nxtNode = None,None
        cur = head

        while cur != None:
            nxtNode = cur.next if cur.next else None
            cur.next = preNode
            preNode = cur
            cur = nxtNode
        
        return preNode
        