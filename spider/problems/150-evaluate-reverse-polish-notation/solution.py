class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        #print('-11'.isdigit())
        for t in tokens:
            if t.isdigit() or t.replace('-','').isdigit():stack.append(t)
            else:
                b,a=stack.pop(),stack.pop()
                print(a+t+b)
                c=eval(a+t+b)
                stack.append(str(int(c)))
        return int(stack[-1])