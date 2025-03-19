# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        left=0
        right=len(height)-1
        while left < right:
            height_area=min(height[left],height[right])
            width=right-left
            max_area=max(max_area,(height_area*width))
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return max_area

        