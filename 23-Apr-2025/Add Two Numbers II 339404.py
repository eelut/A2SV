# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2=[],[]
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
        
        carry=0
        res=None
        while s1 or s2 or carry:
            ans=carry
            if s1:
                ans+=s1.pop()
            if s2:
                ans+=s2.pop()
            node=ListNode(ans%10)
            node.next=res
            res=node
            carry=ans//10
        return res
        