class Solution:

    def encode(self, strs: List[str]) -> str:

        codedStr = ""

        for s in strs:
            length = len(s)
            codedStr += str(length) + "#"  + s
        
        return codedStr + "#"

    def decode(self, s: str) -> List[str]:

        outputList = []

        while len(s) > 1:
            ourHashIndex = s.find("#")
            wordLength = int(s[0:ourHashIndex])
            outputList.append(s[ourHashIndex+1:ourHashIndex+(1+wordLength)])
            s = s[ourHashIndex+(1+wordLength):]
        
        return outputList

