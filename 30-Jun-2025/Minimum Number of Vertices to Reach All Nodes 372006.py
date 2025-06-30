# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        all_nodes = set(range(n))
        
        destination_nodes = set(destination for _, destination in edges)
        
        source_nodes = all_nodes - destination_nodes
        
        return list(source_nodes)