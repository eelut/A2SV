# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        length,tail=1,cur
        while tail.next:
            length +=1
            tail=tail.next
        
        for i in range(length-n-1):
            cur=cur.next
        
        cur.next=cur.next.next
        return dummy.next
        
        