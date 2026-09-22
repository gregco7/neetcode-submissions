class Solution:

    def encode(self, strs: List[str]) -> str:

        codedStr = ""

        for s in strs:
            length = len(s)
            codedStr += str(length) + "#"  + s
        
        return codedStr

    def decode(self, s: str) -> List[str]:

        outputList = []
        i = 0

        while i < len(s):
            ourHashIndex = s.find("#",i)
            wordLength = int(s[i:ourHashIndex])

            i = ourHashIndex + 1
            outputList.append(s[i:i + wordLength])
            i += wordLength
            
        
        return outputList

