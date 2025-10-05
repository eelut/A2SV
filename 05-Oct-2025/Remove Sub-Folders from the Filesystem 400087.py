# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/


class Folder:
    def __init__(self):
        self.children = {} 
        self.end = False 

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Folder()

        res_paths = []
        folder.sort()

        for path in folder:
            tokens = path.split("/")
            is_subfolder = False
            curr = root

            for token in tokens:
                if curr.end:
                    is_subfolder = True
                    break
                if token not in curr.children:
                    curr.children[token] = Folder()
                curr = curr.children[token]
            
            if not is_subfolder:
                curr.end = True
                res_paths.append(path)
        
        return res_paths