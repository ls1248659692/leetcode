class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        li = [list(s) for s in strs]
        li = [[strs[j][i] for j in range(len(strs))] for i in range(len(strs[0]))]
        print(li)
        li = [ len([1 for j in range(1,len(r)) if r[j]<r[j-1]]) for r in li]
        print(li)
        return len([e for e in li if e>0])