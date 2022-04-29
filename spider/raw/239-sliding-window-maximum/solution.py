
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # list1 = []
        # if len(nums) < k:
        #     return nums
        # for i in range(0,len(nums)):
        #     if len(nums[i:i+k]) == k:
        #         list1.append(max(nums[i:i+k]))
        # return list1

        def calc_mxi(b,e):
            mxli = [e-1]
            for i in range(e-2,b-1,-1):
                if ns[i]>ns[mxli[0]]:
                    mxli.insert(0,i)
            return mxli       

        ns=nums
        if k==1:return ns

        mxli = calc_mxi(0,k)    
        res=[mxli[0]]
        print(res,len(mxli),mxli)
        print(len(nums),k)
        #return

        for i in range(k,len(ns)):
            #print('mxli=%s,ns=%s'%(mxli,ns[i-k+1:i+1]))
            if mxli[0]==i-k: mxli=mxli[1:]

            if ns[i]>=ns[mxli[0]]:
                mxli=[i]
            elif ns[i]<ns[mxli[len(mxli)-1]]:
                mxli= mxli+[i]
            else:
                #mxli = [ j for j in mxli if ns[i]<ns[j]]+[i]        
                # mxli = [ mxli[j] for j in range(len(mxli)) if ns[i]<ns[mxli[j]]]+[i]
                             
                # mxlib =[]
                # for j in range(len(mxli)):
                #     if ns[i]<ns[mxli[j]]:
                #         mxlib.append(mxli[j])
                #     else:
                #         break

                # mxlib.append(i)
                # mxli=mxlib

                for j in range(len(mxli)-1,-1,-1):
                    if ns[i]<ns[mxli[j]]:
                        mxli =  mxli[:j+1]+[i]
                        break
            #print(mxli)
            res.append(mxli[0]) 

        print(len(res),res)
        return [ns[i] for i in res]