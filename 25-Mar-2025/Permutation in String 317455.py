# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1) ,len(s2)
        if n2<n1 :
            return False
        freq1,freq2=Counter(s1), Counter(s2[:n1])
        if freq1==freq2:
            return True
        l=0
        for r in range(n1,n2):
            freq2[s2[r]] +=1
            freq2[s2[l]] -=1
            if freq2[s2[l]] ==0:
                del freq2[s2[l]]
            l +=1

            if freq1==freq2:
                return True
        return False
        
