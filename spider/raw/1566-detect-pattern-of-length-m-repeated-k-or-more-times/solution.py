class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if len(arr)<m*k:return False
        for i in range(len(arr)-m*k+1):
            if arr[i:i+m*k]==arr[i:i+m]*k:return True
        return False