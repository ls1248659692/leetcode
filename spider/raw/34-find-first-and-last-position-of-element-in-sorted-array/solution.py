class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def sbin_v0(ar,k):
            if not ar:return -1
            le = len(ar)//2
            if ar[le]==k:return k
            elif ar[le]>k: sbin_v0(ar[le+1:],k)
            else: sbin_v0(ar[:le],k)

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

        def sbin_v11(ar,k,li,f_l):
            if not ar: return -1 if not li else {'f':li[0],'l':li[-1]}[f_l]
            le = len(ar)//2
            if ar[le]==k:
                li.append(le)
                if f_l=='f':
                    nar = ar[:le+1]
                elif f_l=='l':
                    nar = ar[le+1:]
                else: return li[0]
            elif ar[le]>k: nar = ar[le+1:]
            else: 
                nar = ar[:le]
            #print(ar,nar)
            sbin_v11(nar,k,li,f_l)
            return -1 if not li else {'f':li[-1],'l':li[-1]}[f_l]

        def se_seq(nums,target):    
            min_i,max_i=-1,-1
            for ii in range(len(nums)):
                if target==nums[ii]:
                    max_i = ii
                    if min_i==-1: min_i=ii
                elif nums[ii]> target:
                    break
            return min_i,max_i

        li=[]
        def m10(nums,target):
            nonlocal li
            li=[]
            f =sbin_v10(nums,target,0,'f')
            print(f,list(li))
            li=[]
            l =sbin_v10(nums,target,0,'l')
            print(l,list(li))
            return [f,l]

        def m11(nums,target):
            lif =[]
            f=sbin_v11(nums,target,lif,'f')
            lis =[]
            l=sbin_v11(nums,target,lis,'l')        
            print(f,l,lif,lis)

        return m10(nums,target)
        #return se_seq(nums,target)