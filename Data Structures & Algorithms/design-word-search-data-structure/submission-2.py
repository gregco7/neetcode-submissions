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
            res = False

            if (index == len(word)):
                return root.endWord
            
            # for key in map
            for child in root.children:
                if (word[index] == child) or (word[index] == '.'):
                    if dfs(root.children[child],word,index + 1):
                        return True

            return res

        return dfs(self.head,word,0)
                    
              
                

            
            
            
            

            
        
