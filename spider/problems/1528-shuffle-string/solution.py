class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([e[0] for e in sorted(zip(list(s),indices),key=lambda xx:xx[-1])])