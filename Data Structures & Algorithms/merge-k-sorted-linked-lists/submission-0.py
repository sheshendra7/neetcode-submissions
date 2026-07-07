# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        while len(lists)>1:
            first = lists.pop(0)
            second = lists.pop(0)
            tmp = head = ListNode(0)
            while first and second:
                if first.val <= second.val:
                    tmp.next = first
                    first= first.next
                else:
                    tmp.next = second
                    second = second.next
                tmp = tmp.next

            if first:
                tmp.next = first
            if second:
                tmp.next = second
            
            lists.append(head.next)
        
        return lists[0] if len(lists) != 0 else None