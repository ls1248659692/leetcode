class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # 00=1 01=1 10=1  11=0
        #10 1
        r=[first]
        for i,n in enumerate(encoded):
            r.append(r[i]^encoded[i])
        return r