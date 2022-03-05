class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if nums==[0]:return True
        nu,f= nums,len(nums)%2
        def pwin(nu):
            if not nu: r=0
            if len(nu)==1: r= nu[0]
            else:
                if len(nu)%2==f:
                    r =  max(nu[0]+pwin(nu[1:]), nu[-1]+pwin(nu[:-1]))
                else:
                    r =  min(pwin(nu[1:]), pwin(nu[:-1]))
            return r
        return pwin(nu)>=sum(nu)/2