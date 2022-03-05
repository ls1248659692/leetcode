class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums=temperatures
        nls,stk = [0]*len(nums),[]
        ln= len(nums)

        for i in range(ln):
            #print(nums[i],stk)
            while stk and nums[i]>stk[-1][0]:
                nls[stk[-1][1]]=i-stk[-1][1]
                stk.pop()
            stk.append((nums[i],i))
        return nls
          