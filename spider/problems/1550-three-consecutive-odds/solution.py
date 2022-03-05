class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        li =[n%2 for n in arr]
        print(li)
        for i in range(3,len(li)+1):
            if sum(li[i-3:i])==3:return True
        return False