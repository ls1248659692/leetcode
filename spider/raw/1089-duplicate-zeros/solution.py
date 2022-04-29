class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        la_i=0
        zn=0
        for i in range(len(arr)-1,-1,-1):
            if arr[i]!=0 and la_i==0:
                la_i = i
            if la_i and arr[i]==0:
                zn+=1
        print(la_i,zn)
        for i in range(la_i,-1,-1):
            if arr[i]!=0:
                if i+zn <len(arr):arr[i+zn]= arr[i]
            else:
                if i+zn <len(arr):arr[i+zn]=0
                zn -=1
                if i+zn <len(arr):arr[i+zn]=0
        
        
        