class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        nli = [rr.count('1') for rr in bank if rr.count('1')>0]
        print(nli)
        cum=0
        for ii in range(1,len(nli)):
            cum += nli[ii-1]*nli[ii]
        return cum