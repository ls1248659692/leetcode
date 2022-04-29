class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr)%3!=0:return False

        c =0
        s3= sum(arr)//3
        print(s3)
        cnt =0
        # b,e=100000,1000000
        for i in range(len(arr)-1):
            c+=arr[i]
            if c==s3:
                cnt+=1
                c =0
                # break

        # arr = arr[::-1]
        # c=0
        # for i in range(len(arr)):      
        #     c+=arr[i]
        #     if c==s3:
        #         e=i+1
        #         break
        # print(b,e)
        return  cnt>=2