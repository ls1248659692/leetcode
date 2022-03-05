class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        rli=[]
        for i in range(len(boxes)):
            rli.append(sum([abs(i-j) if boxes[j]=='1' and i!=j else 0 for j in range(len(boxes))]))
        return rli
