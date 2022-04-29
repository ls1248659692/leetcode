class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count1,count2 = 0,0
        for i in range(n):
            if s[i] != str(i%2):
                count1 += 1
            else:
                count2 +=1
        return min(count1,count2)