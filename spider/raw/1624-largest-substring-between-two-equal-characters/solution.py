class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_str = -1
        for i in range(len(s)):
            for j in range(len(s)-1,0,-1):
                if s[i] == s[j] and i != j:
                    temp = j - i - 1
                    if max_str < temp:
                        max_str = temp
        return max_str