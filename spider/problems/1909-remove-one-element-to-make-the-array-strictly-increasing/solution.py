class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        badn = [i for i in range(1,len(nums)) if nums[i]-nums[i-1] <=0]
        print(badn)
        if len(nums)<=2 or len(badn)==0 : return True
        if len(badn)==1 and (badn[0]==len(nums)-1 or nums[badn[0]+1]>(nums[badn[0]-1] if badn[0]-1>=0 else -99999)): return True
        if len(badn)==1 and nums[badn[0]]>(nums[badn[0]-2] if badn[0]-2>=0 else -99999): return True
        return False