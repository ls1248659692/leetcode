class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        negpos =1
        if x_str[0]=='-': 
            negpos = -1
            x_str= x_str[1:]
        x_str_rev = ''.join([x_str[ii] for ii in range(len(x_str)-1,-1,-1)])
        #print(x_str_rev,2**31-1)
        x_rev = int(x_str_rev)*negpos
        return 0 if x_rev>2**31-1 else 0 if x_rev<-1*2**31 else x_rev