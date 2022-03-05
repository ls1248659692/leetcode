class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums =sorted(nums)
        n,ln=nums,len(nums)

        def binse(nu,val,left,right):
            #print('binse',val,left,right,nu[left:right])
            while left < right:
                mid =(left+right)//2
                if nu[mid]==val:
                    return mid
                elif nu[mid]<val:
                    left = mid + 1
                else:
                    right = mid
            return left 
        print(n)
        mind=float('inf')
        for i in range(ln-2):
            #if n[i]>target/3:break
            for j in range(i+1,ln-1):
                t2= target-n[i]-n[j]
                if n[j+1]>=t2:
                    mi = t2-n[j+1]
                    #print('bound',mi,t2,n[j+1])
                    if mi==0:return target
                    elif abs(mi)<abs(mind): mind=mi
                    break
                else:
                    mid=binse(n,t2,j+1,ln)
                    #print('mid_return',mid,n[i],n[j],n[mid] if mid<ln else None)
                    a=t2-n[mid] if mid<ln else t2-n[-1]
                    b=t2-n[mid-1] if mid-1<ln else t2-n[-1]
                    mi= a if abs(a)<abs(b) else b
                    #print('bin_bound',mi) 
                    if mi==0:return target
                    elif abs(mi)<abs(mind): mind=mi      
        print(mind)             
        return target-mind