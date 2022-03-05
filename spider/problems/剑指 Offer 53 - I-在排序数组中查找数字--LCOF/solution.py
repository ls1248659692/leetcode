class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def sbin_v10(ar,k,i,f_l):
            if not ar: return -1 if not li else li[-1]
            le = len(ar)//2
            if ar[le]==k:
                li.append(le+i)
                if f_l=='f': nar,ni = ar[:le],i
                elif f_l=='l':nar,ni = ar[le+1:],i+le+1
                else: return li[0]
            elif ar[le]>k: nar,ni = ar[:le],i
            else: nar,ni = ar[le+1:],i+le+1
            #print(ar,nar)
            sbin_v10(nar,k,ni,f_l)
            return -1 if not li else li[-1]

        li=[]
        def m10(nums,target):
            nonlocal li
            li=[]
            f =sbin_v10(nums,target,0,'f')
            print(f,list(li))
            li=[]
            l =sbin_v10(nums,target,0,'l')
            print(l,list(li))
            return l-f+1 if l!=-1 else 0
        return m10(nums,target)        