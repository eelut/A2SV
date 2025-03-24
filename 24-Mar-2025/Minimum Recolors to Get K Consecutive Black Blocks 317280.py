# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_number= float("inf")
        for i in range(len(blocks)-k +1):
            current_value=blocks[i:i+k].count("W")
            min_number=min(min_number,current_value)
        return min_number
        