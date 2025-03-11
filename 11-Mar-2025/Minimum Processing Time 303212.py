# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        n= len(processorTime)
        min_execution_time=0
        for i in range(n):
            assigned_task=tasks[(i*4):(i*4) +4]
            max_assigned_task=max(assigned_task)
            execution_time=processorTime[i] + max_assigned_task

            min_execution_time=max(min_execution_time,execution_time)

        return min_execution_time

            
        
        