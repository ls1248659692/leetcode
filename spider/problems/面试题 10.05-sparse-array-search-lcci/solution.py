class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for i in range(len(words)):
            if words[i]: 
                if words[i]<s:continue
                elif words[i]==s:return i
                else:break
        return -1
