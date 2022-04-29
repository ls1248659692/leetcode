class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        b = [bin(e) for e in arr ]
        s = sorted(b,key=lambda x: x.count('1')*100000+int(x,2))
        return [int(e,2) for e in s]