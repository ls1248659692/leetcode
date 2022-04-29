class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ls = sorted(list(set(letters)))
        print(ls)
        if target>= ls[-1]:return ls[0]
        
        for i in range(len(ls)-1,-1,-1):
            if ls[i]<=target:return ls[i+1]
        return ls[0]