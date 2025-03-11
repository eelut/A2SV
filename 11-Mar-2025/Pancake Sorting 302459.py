# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k=[]
        for i in range(len(arr), 0,-1):
            j= arr.index(i)
            if j+1 == i:
                continue  
            if j != 0:
                k.append(j+1)
            k.append(i)
            arr[:j+1]=reversed(arr[:j+1])
            arr[:i]=reversed(arr[:i])
        return k


        