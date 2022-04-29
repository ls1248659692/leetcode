class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # n = len(nums)
        # li, s, ans =[], '', [False]*n
        # for i in nums:
        #     s += str(i)
        #     if len(s) >1 and s[0] == '0':li.append(int(s[1:],2))
        #     else:li.append(int(s,2))
        # for i in range(n):
        #     if li[i]%5 == 0:
        #         ans[i] = True
        # return ans

        tls=[str(nums[0])]
        for i in range(1,len(nums)):
            tls.append(str(tls[i-1])+str(nums[i]))
        return [int(e,base=2)%5==0 for e in tls]