class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def vpo(po,l,r,mi,mx):
            if (l,r) in cache:return cache[(l,r)]
            #print(l,r)
            if l==r:
                return True
            elif l+1==r:
                return True
            elif l+r==2:
                print('len=2',po[l:r],mi,mx)
                res= min(po[l:r])>mi and max(po[l:r])<mx
            else:
                j= r-2
                while j>=l and po[j]>po[r-1]:j-=1
                    
                # for j in range(r-1,l-1,-1):
                #     if po[j]<po[r-1]:break
                print('break',po[l:r],po[j],j,l)
                if j+1>l:
                    if  max(po[l:j+1])>po[r-1]:
                        print('chke_left',po[l:j+1],po[r-1])
                        res= False
                    else:
                        print(po[l:j+1],po[j+1:r])
                        res= vpo(po,l,j,mi,po[r-1]) and vpo(po,j+1,r-1,po[r-1],mx)
                else:
                    res= vpo(po,j+1,r-1,po[r-1],mx)

            cache[(l,r)]=res
            return res

        cache={}                        
        return vpo(postorder,0,len(postorder),-999999,9999999) if len(postorder)==len(set(postorder)) else False