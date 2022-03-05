class Solution:
    def removeVowels(self, s: str) -> str:
        a = ''
        for i in s:
            if i not in 'aeiou':
                a+=i
        return a