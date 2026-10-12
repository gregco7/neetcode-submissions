class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class PrefixTree:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        current = self.node
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.endWord = True

    def search(self, word: str) -> bool:
        current = self.node
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.endWord

    def startsWith(self, prefix: str) -> bool:
        current = self.node
        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]
        return True
        
        