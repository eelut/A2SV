# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while fast:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            tmp=slow
            slow=slow.next
            tmp.next=prev
            prev=tmp
        
        first,second=head,prev
        max_sum=0
        while second:
            max_sum=max(max_sum,first.val+second.val)
            first=first.next
            second=second.next
        return max_sum
        
        