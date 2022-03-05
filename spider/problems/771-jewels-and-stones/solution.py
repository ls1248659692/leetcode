class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len ([s for s in stones if s in jewels])