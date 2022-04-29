class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = 0
        res = ''
        for i in s:
            if i == '(':
                stk += 1
                if stk >1:
                    res += '('
            else:
                stk -=1
                if stk != 0:
                    res += ')'
        return res