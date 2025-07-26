# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def backtrack(node, path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append('->'.join(path))
            else:
                backtrack(node.left, path)
                backtrack(node.right, path)
            path.pop()  # backtrack

        result = []
        backtrack(root, [])
        return result
