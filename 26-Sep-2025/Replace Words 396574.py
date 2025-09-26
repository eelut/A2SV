# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word_end += 1

    def replaceWord(self, word):
        node = self.root
        idx = 0
        for ch in word:
            if ch not in node.children:
                return word
            node = node.children[ch]
            idx += 1
            if node.word_end != 0:
                return word[:idx]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        ans = []
        for word in sentence.split():
            ans.append(trie.replaceWord(word))
        return ' '.join(ans)