class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binse(ls,tg):
            l,r=0,len(ls)
            while l<r:
                m= (l+r)//2
                if ls[m]==tg:return m
                elif ls[m]<tg: l=m+1
                else: r=m
            return -1

        def binse_v1(ls,tg):
            l,r=0,len(ls)
            while l<r:
                m= (l+r)//2
                if ls[m]==tg:return 1,m
                elif ls[m]<tg: l=m+1
                else: r=m
            return 0,l        
        status,pos= binse_v1(nums,target)
        return pos if status else pos