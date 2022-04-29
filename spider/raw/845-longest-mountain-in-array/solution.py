class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)==1:return 0
        #arr = [float('inf')]+arr+[float('inf')]
        # arr = arr + [float('inf')] if arr[-2]>arr[-1] else arr+[float('-inf')]
        nu,mx=  arr,0
        p= 0 if nu[1]>nu[0] else 1
        for i in range(1,len(nu)-1):
            b, e = i, i
            if (nu[i]-nu[i-1]) > 0 and (nu[i+1]-nu[i]) < 0:
                while b - 1 >= 0 and nu[b] > nu[b-1]:
                    b -= 1
                while e + 1 < len(nu) and nu[e] > nu[e+1]:
                    e += 1
                mx = max(mx, e-b+1)
        return mx