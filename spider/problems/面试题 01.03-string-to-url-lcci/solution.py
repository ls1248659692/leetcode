class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        nl = S.count(' ')*2+length
        return S[:length].replace(' ','%20')[:nl] if S.strip() else S[:length].replace(' ','%20')