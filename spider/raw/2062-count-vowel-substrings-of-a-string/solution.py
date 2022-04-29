class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        for i in range(len(word)):
            for j in range(len(word)+1):
                if i != j and sorted(set(word[i:j])) == ['a', 'e', 'i', 'o', 'u']:
                    count = count + 1
        return count