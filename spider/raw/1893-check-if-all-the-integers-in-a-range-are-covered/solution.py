class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ele = []
        for i in ranges:
            ele = ele + list(range(i[0], i[1]+1))
        for i in range(left, right + 1):
            if i not in ele:
                return False
        return True