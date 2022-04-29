class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nu =nums[:]
        def nxtv(ls,v):
            for n in sorted(ls):
                if n>v: return n

        for i in range(len(nu)-2,-1,-1):
            mxnu = sorted(nu[i:],reverse=True)
            if nu[i:]== mxnu :
                if i==0:
                    minu = sorted(nu)
                    for j in range(i,len(minu)): nums[j]=minu[j]
            else:
                nv=nxtv(mxnu,nu[i])
                print('i',i,mxnu,nv)
                if nv is not None :
                    nums[i]=nv
                    mxnu.remove(nv)
                    nv2=sorted(mxnu[:])
                    print(nums,nv2)
                    for j in range(len(nv2)): nums[i+1+j]=nv2[j]
                    break


