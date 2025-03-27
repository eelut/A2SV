# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        if n==1:
            return 1
        l=0
        ans=1

        for r in range(1,n):
            cmp = (arr[r - 1] > arr[r]) - (arr[r - 1] < arr[r])  

            if cmp == 0:  
                l = r
            elif r == n - 1 or (cmp * ((arr[r] > arr[r + 1]) - (arr[r] < arr[r + 1]))) != -1:
                ans = max(ans, r - l + 1)
                l = r  

        return ans