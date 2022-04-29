class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        target = [tuple(i) for i in target]  
        for i in range(3): 
            mat = list(zip(*mat))[::-1]
            if mat == target:
                return True 
        return False
        