class Solution:
    def findPeakElement(self, nu: List[int]) -> int:
        nu=[float('-inf')] + nu + [float('-inf')]
        # if len(nu)==1:return 0
        # if len(nu)==2: return 0 if nu[0]>nu[1] else 1
        for i in range(1,len(nu)):
            if nu[i-1]<nu[i]>nu[i+1]:return i-1