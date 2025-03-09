# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged=[intervals[0]]

        for i in range (1,len(intervals)):
            prev=merged[-1]
            curr=intervals[i]

            if prev[1] >= curr[0]:
                prev[1]=max(prev[1],curr[1])
            else:
                merged.append(curr)

        return merged




        