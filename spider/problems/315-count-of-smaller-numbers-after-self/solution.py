class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ln,res,sub = len(nums),[0],[nums[-1]]
        def binse(nu,val,left,right):
            while left < right:
                mid =(left+right)//2
                if nu[mid]>=val:
                    left = mid + 1
                else:
                    right = mid
            return left

        print(ln)
        for i in range(ln-2,-1,-1):
            mid = binse(sub,nums[i],0,ln-1-i)
            # sub = sub[:mid] + [nums[i]] + sub[mid:]
            sub.insert(mid,nums[i])
            #print(sub)
            res.append(ln-1-i-mid)
        return res[::-1]