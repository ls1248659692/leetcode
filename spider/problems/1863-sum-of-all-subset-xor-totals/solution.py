class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # def sbs(nums):
        #     if not nums:return []
        #     if len(nums)==1: return [[nums[0]],[]]
        #     n1=sbs(nums[1:])
        #     return [[nums[0]] +e for e in n1] +n1
        # sbset =sbs(nums)
        # print(sbset)
        # r = 0
        # for s in sbset:
        #     if not s:continue
        #     x=s[0]
        #     for n in s[1:]:
        #         x =x^n
        #     r+=x
        # return r
        xorls=lambda x: 0 if not x else x[0]^xorls(x[1:])
        ns= [[]]
        for num in nums:
            ns += [[num]+ss for ss in ns]
        return sum( xorls(ls) for ls in ns)
        # for num in nums:
        #     ns += [num ^ ss for ss in ns]
        # return sum(n_s)
        #3 1:6 2:6 3:6
        #4 1:10 2:12 3:14 4:8
        #5 1:10 2:14 3:14 4:10 5:10 6:14 7:14 8:26 9:26 10:30 12:26 14:30 16:42
        #6 1:14 2:12 3:14 4:12 5:14
        #7 1:14 2:14 3:14 4:14 5:14
        #8 1:18 2:20 3:22 4:24 5:26
        #9 1:18 2:22 3:22 4:26 5:26

        #10 1:22 2:20 3:22 4:28 5:30
        #15 1:30 2:30 3:30 4:30 5:30
        #16 1:34 2:36 3:38 4:40 5:42
        #17 1:34 2:38 3:38 4:42 5:42