class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        res = []
        for a in arr:
            for p in pieces:
                if a and p and a != p[0]: continue
                res.extend(p)
        return arr == res