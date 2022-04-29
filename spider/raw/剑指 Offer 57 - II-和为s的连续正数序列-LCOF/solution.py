class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        return [list(range((target*2//qq-qq+1)//2,(target*2//qq-qq+1)//2+qq)) for qq in range(int((target*2)**0.5),1,-1) if target*2%qq==0 and (qq+target*2//qq)%2==1]