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
        curr = self.head
        
        def dfs(root,word,index): # e.g .ay would search ay from head roots children
            res = False

            if (index == len(word) - 1) and ((word[index] in root.children) or word[index]=='.'):
                if word[index] == '.':
                    for child in root.children:
                        if root.children[child].endWord:
                            return True
                    return False
                else:
                    return root.children[word[index]].endWord
            
            # for key in map
            for child in root.children:
                if (word[index] == child) or (word[index] == '.'):
                    res = res or dfs(root.children[child],word,index + 1)

            return res

        return dfs(self.head,word,0)
                    
              
                

            
            
            
            

            
        
