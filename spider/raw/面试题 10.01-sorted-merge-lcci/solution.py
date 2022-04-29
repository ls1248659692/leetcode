class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        #ta=None
        #return ta is None

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if B[j] is None :continue
                if A[i]<B[j]:
                    A[i+j+1]=B[j]
                    B[j]=None
                else:
                    A[i+j+1]=A[i]
                    #A[i]=-1
                    break
        for j in range(n-1,-1,-1):
            if B[j] is not None:A[j]=B[j]
        return A
