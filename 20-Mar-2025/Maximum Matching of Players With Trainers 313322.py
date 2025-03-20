# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        j=0
        res=0
        for i in range(len(players)):
            while j <len(trainers) and players[i]> trainers[j]:
                j += 1
            if j <len(trainers) and players[i] <= trainers[j]:
                res +=1
                j +=1
        return res