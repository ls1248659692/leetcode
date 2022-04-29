class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a,b = aliceSizes,bobSizes
        d =(sum(a)-sum(b))//2
        sa,sb=set(a),set(b)
        return [(e,e-d) for e in sa if e-d in sb][0]