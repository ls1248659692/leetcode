class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        from collections import Counter
        ct=Counter(s).most_common()
        abcsingle=[e for e in ct if e[1]%2==1]
        return len(abcsingle)<=k and len(s)>=k