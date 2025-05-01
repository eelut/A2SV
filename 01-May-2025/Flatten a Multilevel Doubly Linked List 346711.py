# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node=head
        while node:
            if node.child:
                old_next=node.next
                node.next=self.flatten(node.child)
                node.next.prev=node
                node.child=None

                while node.next:
                    node=node.next
                
                node.next=old_next
                if old_next:
                    old_next.prev=node
            node=node.next
        return head
        