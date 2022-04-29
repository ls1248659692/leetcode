class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i in range(len(nums)):
            dic.setdefault(nums[i],[i,99999999])
            if dic[nums[i]][0]==-1:dic[nums[i]][0]=i
            if i>dic[nums[i]][0] and (i-dic[nums[i]][0]<dic[nums[i]][1]):
                dic[nums[i]][1]= i - dic[nums[i]][0]
                dic[nums[i]][0]=i
        print(dic)
        for n,ij in dic.items():
            i,j = ij
            if j <=k:return True
        return False
