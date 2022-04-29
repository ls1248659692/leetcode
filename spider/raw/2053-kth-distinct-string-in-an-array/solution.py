class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dli= [el for el in arr if arr.count(el)==1]
        return '' if k-1>=len(dli) else dli[k-1]