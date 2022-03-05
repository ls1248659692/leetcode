class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:return max(nums)

        def v1(nu):
            ln = len(nu)
            print(nu)
            if ln<2:return max(nu)
            f3,f2,f1=0,nu[0],nu[1]
            for i in range(2,ln):
                f3,f2,f1=f2,f1,max(nu[i]+f3,nu[i]+f2)
                print(f3,f2,f1)
            return max(f2,f1)
        return max(nums[0]+v1(nums[2:-1]),v1(nums[1:]))