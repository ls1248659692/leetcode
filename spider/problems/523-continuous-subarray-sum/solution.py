class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2:return False
        cli= [nums[0]%k]
        for n in nums[1:]:cli.append((cli[-1]+n)%k)
        d={}
        for i in range(len(cli)):
            c = cli[i]
            d.setdefault(c,[i,i])
            d[c][-1]=i
            if c==0 and i>=1:return True
            if d[c][-1]-d[c][0]>=2:return True
        print(cli,d)
        return False    
        # print(cli)
        #return sum(1 for c in range(k) if cli.count(c)>=2)>0 or (0 in cli)
            