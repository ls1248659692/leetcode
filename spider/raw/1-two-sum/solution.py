class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for ii in range(len(nums)-1):
        #     if target - nums[ii] in nums[ii+1:]:
        #         jj= nums.index(target - nums[ii],ii+1) 
        #         return [ii,jj]
        #if target%2==0 and nums.count(target//2)>=2: return nums.index(target//2),len(nums)-1-nums[::-1].index(target//2)
        r_nums_set = set([target - nn for nn in nums])
        rr = [ii for ii in range(len(nums)) if nums[ii] in r_nums_set]
        return rr if len(rr) == 2 else [ii for ii in rr if nums[ii] * 2 != target]

        dic = {num:idx for idx,num in enumerate(nums)}
        return [[i,dic.get(target-n,-1)] for i,n in enumerate(nums) if dic.get(target-n,-1)!=-1 and i!=dic.get(target-n,-1)][0]

        return  [[i,nums.index(target - n,i+1)] for i,n in enumerate(nums) if target-n in nums[i+1:]][0]
        return [[i,len(nums)-1-nums[::-1].index(target-n)]  for i,n in enumerate(nums) if target-n in nums and i!=len(nums)-1-nums[::-1].index(target-n)][0]
        #if target%2==0 and nums.count(target//2)>=2: return nums.index(target//2),len(nums)-1-nums[::-1].index(target//2)
            # ts= list(set([target-n for n in nums])& set(nums))[0]
            # return [nums.index(ts),len(nums)-1-nums[::-1].index(target-ts)]     
        #print([[i,len(nums)-1-nums[::-1].index(target-n)]  for i,n in enumerate(nums) if target-n in nums])

 


        return sorted([[i,len(nums)-1-nums[::-1].index(target-n)]  for i,n in enumerate(nums) if target-n in nums],key=lambda x:max(x)-min(x))[-1]