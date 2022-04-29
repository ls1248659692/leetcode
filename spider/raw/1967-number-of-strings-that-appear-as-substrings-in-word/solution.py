class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum ([1 if pp in word else 0 for pp in patterns])