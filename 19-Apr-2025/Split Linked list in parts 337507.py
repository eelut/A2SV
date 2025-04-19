# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length,curr=0,head
        while curr:
            curr =curr.next
            length +=1
        normal_length,extra_length=length//k,length%k
        curr=head
        ans=[]
        for i in range(k):
            ans.append(curr)

            for j in range(normal_length-1 +(1 if extra_length else 0)):
                if not curr:
                    break
                curr=curr.next
            extra_length -=1 if extra_length else 0
            if curr:
                curr.next,curr=None,curr.next
        return ans
