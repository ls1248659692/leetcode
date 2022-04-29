class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for y in matrix:
            for x in y:
                if x == target:
                    return True
        return False