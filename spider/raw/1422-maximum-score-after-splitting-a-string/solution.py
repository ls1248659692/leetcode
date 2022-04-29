class Solution:
    def maxScore(self, s: str) -> int:
        count_rec = 0 
        for i in range(1,len(s)):

            count = 0 
            str1 = s[0:i]
            str2 = s[i::]
            for x in str1:
                if x == '0':
                    count = count+1
            for y in str2:
                if y == '1':
                    count = count +1
            if count > count_rec:
                count_rec = count
        return count_rec
            
