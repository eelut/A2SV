# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        total=0
        for x,freq in count.items():
            size=x+1
            groups=math.ceil(freq/size)
            total+=groups*size
        return total
        