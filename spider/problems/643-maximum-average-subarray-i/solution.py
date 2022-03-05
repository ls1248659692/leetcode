class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)<=k:return sum(nums)/k
        avgli = [sum(nums[:+k])/k]#[sum(nums[i:i+k])/k for i in range(0,len(nums)-k+1)]
        for i in range(1,len(nums)-k+1): 
            print(nums[i+k-1])
            #avgli.append(sum(nums[i:i+k])/k)
            avgli.append(avgli[-1]+nums[i+k-1]/k-nums[i-1]/k)
        print(avgli)    
        return max(avgli)
            

        # list_ave = []
        # if len(nums)<=k:
        #     return sum(nums)/k
        # for i in range(len(nums)):
        #     if len(nums[i:i+k]) == 4:
        #         if sum(list_ave)<sum(nums[i:i+k]):
        #             list_ave = nums[i:i+k]
        
        # return((sum(list_ave))/k)
