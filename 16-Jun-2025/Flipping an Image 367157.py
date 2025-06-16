# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for im in image:
            im.reverse()
        for im in image:
            for i in range(len(im)):
                if im[i] == 0:
                    im[i]+=1
                elif im[i] == 1:
                    im[i]-=1
        return image 

        