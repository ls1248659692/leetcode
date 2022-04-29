class Solution:
    def convertToBase7(self, num: int) -> str:
        cli=[]
        s= '-' if num<0 else ''
        num = abs(num)
        while num>=7:
            cli.append(num%7)
            num = num//7
        cli.append(num)
        return s+''.join([str(e) for e in cli[::-1]])