class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set([arr.count(n) for n in set(arr)])) == len(set(arr))