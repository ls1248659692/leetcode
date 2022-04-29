class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words = sorted(words , key =len)
        a = ''.join(sorted([i.lower() for i in licensePlate if i.isalpha() and i.isdigit() == False] , key = len))
        count = collections.Counter(a)
        for i in words:
            if not count - collections.Counter(i):
                return i