class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        def v1(matrix):
            mtr,tg = matrix,target
            while mtr and mtr[0]:
                m,n = len(mtr[0]),len(mtr)
                print(m,n)
                tij = -2 if mtr[0][0]<=target<=mtr[-1][-1] else -1
                if tij==-1:return False
                for i in range(m):
                    if mtr[0][i]==tg:return True
                    elif mtr[0][i]>tg:break
                for ii in range(m):
                    if mtr[-1][ii]==tg:return True
                    elif mtr[-1][ii]>tg:break                
                for j in range(n):
                    if mtr[j][0]==tg:return True 
                    elif mtr[j][0]>tg:break       
                for jj in range(n):
                    if mtr[jj][-1]==tg:return True 
                    elif mtr[jj][-1]>tg:break 
                print(i,ii,j,jj)              
                mtr = [ mtr[tj][ii:i] for tj in range(jj,j)]    
                for r in mtr:print(r)
            return False  
        return v1(matrix)

        def v0(matrix):
            def sbin_v10(ar,k,i,f_l):
                if not ar: return -1 if not li else li[-1]
                le = len(ar)//2
                if ar[le]==k:
                    li.append(le+i)
                    if f_l in ['f','f>']: nar,ni = ar[:le],i
                    elif f_l in ['l','l>']:nar,ni = ar[le+1:],i+le+1
                    else: return li[0]
                elif ar[le]>k: 
                    if f_l in ['f>']: li.append(le+i)
                    nar,ni = ar[:le],i
                else: 
                    if f_l in ['l>']: li.append(le+i)
                    nar,ni = ar[le+1:],i+le+1
                #print(ar,nar)
                sbin_v10(nar,k,ni,f_l)
                return -1 if not li else li[-1]

            li=[]
            def m10(nums,target,eq_btw):
                nonlocal li
                li=[]
                f =sbin_v10(nums,target,0,'f'+eq_btw)
                print('f',f,list(li))
                li=[]
                l =sbin_v10(nums,target,0,'l'+eq_btw)
                print('l',l,list(li))
                return l
            if  matrix in ([],[[]]):return False
            mc= m10(matrix[0],target,'>') 
            ar2 = [matrix[i][mc] for i in range(len(matrix))] 
            mr = m10(ar2,target,'')
            return mr!=-1