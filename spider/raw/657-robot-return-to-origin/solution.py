class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        ans = 0
        for i in moves:
            if i == "U":
                ans += 1
            elif i == 'D':
                ans -= 1
            elif i == 'L':
                ans += 1j
            else:
                ans -= 1j
        return True if ans == 0 else False