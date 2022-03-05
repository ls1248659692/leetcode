class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        def dsplit(s):
            r = [s[0]]
            for c in s[1:]:
                if c != r[-1][-1]:
                    r.append(c)
                else:
                    r[-1] += c
            return r       
        r = dsplit(''.join([str(e) for e in nums]))
        print(r)
        return max([len(e) for e in r if e[0]=='1']) if 1 in nums else 0