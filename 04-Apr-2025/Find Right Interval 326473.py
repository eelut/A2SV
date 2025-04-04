# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

from bisect import bisect_left
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
    
        start_with_index = sorted((start, i) for i, (start, end) in enumerate(intervals))
    
        starts = [start for start, i in start_with_index]
    
        result = []
    
        for interval in intervals:
            end = interval[1]
            idx = bisect_left(starts, end)
            if idx < n:
                result.append(start_with_index[idx][1])
            else:
                result.append(-1)
        return result
       
        
        
        
        
        
            
        
            
    
    
    

        