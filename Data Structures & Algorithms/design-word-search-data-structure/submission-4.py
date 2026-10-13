class TrieNode():
    def __init__(self):
        self.children = {}
        self.endWord = False
       

class WordDictionary:
    def __init__(self):
        self.head = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]     
        curr.endWord = True

    def search(self, word: str) -> bool:
        
        def dfs(root,word,index): # e.g .ay would search ay from head roots children
            if (index == len(word)):
                return root.endWord
            
            # Only loop if you have to (i.e), the character is a dot
            if (word[index] == '.'):
                 for child in root.children:
                    if dfs(root.children[child],word,index + 1):
                        return True

            if (word[index] in root.children):
                if dfs(root.children[word[index]],word,index + 1):
                        return True

            return False

        return dfs(self.head,word,0)
                    
              
                

            
            
            
            

            
        
