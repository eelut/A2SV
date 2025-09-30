# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_num_contain = set()


class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str, num: int) -> None:
        n = len(word)
        for i in range(n):
            node = self.root
            for j in range(i, n):
                node = node.children[word[j]]
                node.word_num_contain.add(num)


    def search(self, word: str) -> List[str]:
        n = len(word)
        res = []
        for i in range(n):
            node = self.root
            cur_str = ""
            for j in range(i, n):
                cur_str += word[j]
                node = node.children[word[j]]
                if len(node.word_num_contain) == 1: 
                    res.append(cur_str)
                    break
        return sorted(res, key=lambda x: (len(x), x))[0] if res else ""


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        t = Trie()
        for i, word in enumerate(arr): t.insert(word, i)

        return [t.search(word) for word in arr]