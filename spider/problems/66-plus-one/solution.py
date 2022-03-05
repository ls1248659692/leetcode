class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # def v0(digits):
        #     nli=[]
        #     if not digits: return None
        #     up_1b = digits[-1]==9
        #     for ii in range(len(digits)-1,-1,-1):
        #         if 9==digits[ii] and up_1b:
        #             nli.append(0)
        #             up_1b=True
        #         else:
        #             nli.append(digits[ii]+ (1 if up_1b or not nli else 0))
        #             up_1b= False
        #     if up_1b: nli.append(1)
        #     nli.reverse()
        #     return nli

        # add = lambda digits: [1, 0] if digits == [9] else ((digits[:-1] + ([digits[-1] + 1])) if digits[-1] != 9 else (add(digits[:-1]) + [0]))
        plusone = lambda d:[1,0] if d==[9] else  plusone(d[:-1]) + [0] if d[-1]==9 else d[:-1] + [d[-1] + 1]
        return plusone(digits)

        #return [(d+1)%10 if set(digits[i+1:]) in (set([9]),set([])) else d for i,d in enumerate(digits)] if set(digits)!=set([9]) else  [1]+[0]*len(digits)
