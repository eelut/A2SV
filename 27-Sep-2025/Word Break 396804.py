# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class TrieNode:
    def __init__(self, character=None):
        self.character = character
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children.update({char: TrieNode(char)})
            current = current.children.get(char)
        current.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            try:
                current = current.children[char]
            except KeyError:
                return False
        if current.is_end_of_word:
            return True
        else:
            return False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        cache = {}
        def traverse(s, trie):
            if s in cache:
                return cache[s]
            if len(s) == 0:
                cache[s] = True
                return True
            for i in range(len(s)):
                if trie.search(s[:i+1]) and traverse(s[i+1:], trie):
                    cache[s] = True
                    return True
            cache[s] = False
            return False
        return traverse(s, trie)

        