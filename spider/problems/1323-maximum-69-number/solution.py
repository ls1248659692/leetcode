class Solution:
    def maximum69Number (self, num: int) -> int:
        nli=list(str(num))
        print(nli)
        for i in range(len(nli)):
            if nli[i]=='6':
                nli[i]='9'
                break
        return int(''.join(nli))