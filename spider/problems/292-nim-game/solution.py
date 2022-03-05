class Solution:
    def canWinNim(self, n: int) -> bool: #s8
        if n in [1,2,3]:return True
        elif n in [4,]:return False
        elif n in [5,6,7]:return True
        elif n in [8]:return False
        else:
            return  n%4 in [1,2,3]