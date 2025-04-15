# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total=sum(skill)
        
        if total %(len(skill)//2):
            return -1
        
        count =Counter(skill)
        target=total //(len(skill)//2)
        res=0

        for s in skill:
            if not count[s]:
                continue

            diff=target-s
            if not count[diff]:
                return -1
            res+=diff *s
            count[s]-=1
            count[diff]-=1
        return res