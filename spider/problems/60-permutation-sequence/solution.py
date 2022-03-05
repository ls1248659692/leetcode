class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def v1(n,k):
            ca={}
            vis=[]
            def perm(first=0):
                if len(res)>k:return
                if first ==n:
                    res.append(nums[:])
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    perm(first + 1)
                    nums[first], nums[i] = nums[i], nums[first] # æ¤éæä½
            res =[]
            nums = [i for i in range(1,n+1)]
            perm()
            rr= sorted([ls for ls in res])[k-1]
            return ''.join(map(str,rr))

        def v0(nums,k):
            ca={}
            def perm(nums):
                if len(res)>k:return []
                tnu = tuple(nums)
                ln = len(nums)
                if tnu in ca: return ca[tnu]
                if ln<=1:
                    r= [nums]
                else:
                    r = []
                    for ii in range(ln):
                        tli = [ [nums[ii]] + el for el in perm(nums[:ii]+nums[ii+1:])]
                        for el in tli: 
                            r.append(el)
                            if ln ==n and len(res)<=k:
                                res.append(el)
                ca[tnu]=r
                return r     
            res=[]
            #nums = [i for i in range(1,n+1)]
            r=perm(nums)
            rr= sorted([ls for ls in r])[k-1]
            return ''.join(map(str,rr))

        if n<9:
            return v0([i for i in range(1,n+1)],k)
        else:
            fa8 = math.factorial(8)
            print(fa8)
            m =k//fa8
            lft= k%fa8
            return str(m+1)+v0([i for i in range(1,n+1) if i!=m+1],lft)