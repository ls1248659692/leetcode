class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n)) <= 3:
            return str(n)
        a = list(reversed(str(n)))
        cnt = 0
        for i in range(3,len(a),3):
            a.insert(i+cnt,'.')
            cnt += 1
     

        return ''.join(list(reversed(a)))