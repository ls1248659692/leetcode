class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        tli = [releaseTimes[i] -(0 if i==0 else releaseTimes[i-1]) for i in range(len(releaseTimes))]
        #tmax = 
        return  sorted([keysPressed[i] for i in range(len(tli)) if tli[i]==max(tli)])[-1]