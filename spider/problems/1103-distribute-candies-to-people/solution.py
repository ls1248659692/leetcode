class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # r--> first_distribut , 
        n =num_people
        distribute = n*(n+1)//2
        cnt = 0
        while candies > distribute:
            candies -= distribute
            distribute += n*n
            cnt += 1
        print(candies,cnt)
        # bli_o = [((i+1)*cnt+ n*(cnt-1)) if cnt>=1 else 0 for i in range(n)]
        bli = [(i+i+n*(cnt-1))*cnt//2 for i in range(1,n+1)]
        # print(bli_o)
        print(bli)

        if cnt == 0 or candies >= 1+cnt*n:
            cli = [1+cnt*n]
            candies -= cli[-1]
            print(cli,candies)
            while candies > cli[-1]:
                print(cli,candies)
                cli.append(int(cli[-1]+1))
                candies -= int(cli[-1])
                print(cli,candies)
            cli.append(int(candies))
            print(cli)
        else:
            cli = [candies]
                
        cli =cli+[0 for j in range(n-len(cli))]
        
        res = [int(bli[i]+cli[i]) for i in range(len(bli))]
        return res