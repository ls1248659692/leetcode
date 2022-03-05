# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mininum = 1
        maxnum = n
        while mininum <= maxnum:
            numguess = (mininum + maxnum) // 2
            if guess(numguess) == 0:
                return numguess
            elif guess(numguess) == -1:
                maxnum = numguess - 1
            elif guess(numguess) == 1:
                mininum = numguess + 1