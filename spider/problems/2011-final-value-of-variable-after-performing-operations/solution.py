class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if '++' in op else -1 for op in operations )