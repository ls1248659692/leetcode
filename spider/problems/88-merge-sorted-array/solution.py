class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_ii=0
        for nn in range(len(nums2)):
            n2=nums2[nn]
            #print('check_n2=%d'%n2)
            append=False
            for ii in range(last_ii,m+n):
                if n2<=nums1[ii]:
                    for jj in range(m+nn-1,ii-1,-1):
                        nums1[jj+1]=nums1[jj]
                    nums1[ii]=n2
                    last_ii =ii
                    #print(nums1)
                    break
                elif ii>=m+nn:
                    append=True
                    break
                else:
                    continue
            if append:
                nums1[nn-n]=n2