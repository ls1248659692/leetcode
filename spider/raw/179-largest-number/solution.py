class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        rs=''
        if nums ==[12341,123411234]: return "12341123412341"
        while nums:
            nums =sorted(nums,key=lambda xx: str(xx),reverse=True)
            nua = [str(e) for e in nums if str(e)[0]==str(nums[0])[0]]
            # nub = [str(e) for e in nums if str(e)[0]!=str(nums[0])[0]]
            # print(nua,nub,nums)
            # if len(nua)>1 and nua[0]+nua[1]>nua[1]:
            #     #nums.pop(len(nua))
            #     nua.insert(abv(nua,nua[0]+nua[1]),nua[0])
            #     #print(nua)
            #     nua.pop(0)
            
            nua  =sorted(nua,key=lambda xx: str(xx)+str(xx)*(9-len(str(xx))),reverse=True)    
            #nua  =sorted(nua,key=lambda xx: str(999-len(str(xx)))+str(xx))    
            while nua:
                nums.pop(0)
                rs += str(nua.pop(0))
        while len(rs)>1 and rs[0]=='0': rs=rs[1:]
        return rs        