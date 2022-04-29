class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        r=[]
        def pans(nu):
            mx=max(nu)
            midx= nu.index(mx)
            if len(nu)>1:
                if midx!=0:
                    r.append(midx+1)
                    nu=nu[:midx+1][::-1]+nu[midx+1:]
                r.append(len(nu))
                nu=nu[::-1]
                print(nu)
                pans(nu[:-1])
        pans(arr)
        return r