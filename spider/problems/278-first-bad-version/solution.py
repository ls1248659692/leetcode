# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def v0(n):
            # step,mi,mx = n//2,n//2,n
            for i in range(n,-1,-1):
                if not  isBadVersion(i):return i+1
        
        def v1(n):
            left, right = 0, n
            while left < right:
                mid = (left+right) //2
                if not isBadVersion(mid) and isBadVersion(mid+1):
                    return mid +1
                elif not isBadVersion(mid) and not isBadVersion(mid-1):
                    left = mid
                else:
                    right = mid
        #return v1(n)

        def v1b(n):
            left, right = 1, n
            while left < right:
                mid = (left+right) //2
                if not isBadVersion(mid):
                    left = mid +1
                else:
                    right = mid 
            return left
            
        return v1b(n)  

        def v2(n):
            i = 1
            while isBadVersion(i) == False:
                i = (n + i)//2 if (n+i) % 2 == 0 else (n + i - 1)//2
            return i 