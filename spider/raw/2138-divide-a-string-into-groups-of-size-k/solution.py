class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s = s + fill*(k-len(s)%k) if len(s)%k != 0 else s
        li = []
        for i in range(0,len(s),k):
            li.append(s[i:i+k])
        return li