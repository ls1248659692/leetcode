class Solution:
    def reformat(self, s: str) -> str:
        # stk,ans = 0,''
        # for i in s:
        #     if i.isdigit() and stk == 0:
        #         ans += i
        #         stk += 1
        #     else:
        #         ans += i
        #         stk -= 1
        # if not ans.isdigit() or ans.isalpha():
        #     return ans
        # else:
        #     return ''

            # change another way

        ns = [ ch for ch in s if ch in '0123456789']
        abcs = [ ch for ch in s if ch not in '0123456789']
        mx,mi = (ns,abcs) if len(ns)>len(abcs) else (abcs,ns)
        return ''.join([mx[i]+(mi[i] if i<len(mi)else '') for i in range(len(mx))])  if abs(len(abcs)-len(ns))<=1 else ''

        
        ns = [ ch for ch in s if ch in '0123456789']
        abcs = [ ch for ch in s if ch not in '0123456789']
        min_l = min(len(ns),len(abcs))
        if abs(len(abcs)-len(ns))>1:return ''
        mid=''.join([ns[i]+abcs[i] for i in range(min_l)])
        if len(abcs) < len(ns):
            abcs , ns = ns , abcs
            left = ns[-1]
            return  mid+left 
        else:return mid
