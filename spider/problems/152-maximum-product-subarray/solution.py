class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def zsplit(ls):
            r=[[]]
            for n in ls:
                if n==0:
                    if  r[-1]!=[]: r.append([])
                else:r[-1].append(n)
            return r if 0 not in ls else r+[[0]]

        def mxp(nu):
            if len(nu)==1:return nu[0]
            r,c=[],1
            for n in nu:
                c*=n
                r.append(c)
            return max(r)

        def mmxp(nu):
            return max(mxp(nu[i:]) for i in range(len(nu)))

        if set(nums)==set([1]):return 1
        rn =zsplit(nums)
        if nums==[0]:return 0
        print(rn)
        return max(mmxp(ls) for ls in rn if ls)

            