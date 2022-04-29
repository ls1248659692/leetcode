class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = 0
        while idx < len(word):
            if word[idx] != ch:
                idx += 1
            else: break
        ans = word[:idx+1][::-1]+word[idx+1:]
        return ans if ch in word else word