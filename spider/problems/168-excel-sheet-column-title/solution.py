class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def v3(columnNumber):
            ans =''
            # print((columnNumber-1)%26)
            while columnNumber:
                ans = chr((columnNumber-1)%26 +ord('A')) + ans
                columnNumber = (columnNumber -(columnNumber-1)%26)//26
            return ans
        #return v3(columnNumber)

        def v2b(columnNumber):
            cn,ans= columnNumber,''
            az=lambda x: 26 if x%26==0 else x%26
            while cn :
                ans += chr(az(cn)-1+ord("A"))
                cn= (cn- az(cn))//26
            return ans [::-1]      
        return v2b(columnNumber)        

        def v1(columnNumber):
            #1,26   26*1+1, 26**1*26+26**0*26     26**2*1+26+1, 26**2*26 + 26**1*26 + 26**0*26
            #1,26 26+1, 26*27,  26*26*26+26*27=26*(26*26+1) 26***4 +26**3 +26**2 +26**1 = 26*(26*26*26+26*26+1)
            # 26 26*(26+1) 26*(26*26+1) 26*(26**2+26**1 + 26**0)

            cn= columnNumber
            bas =[1]
            for ii in range(1,10):
                if bas[-1]+26**ii>2**31-1:break
                bas.append(bas[-1]+26**ii)
            print(bas)
            tbas= [26]
            for jj in range(1,len(bas)-1):
                tbas.append(26**jj*26+tbas[-1])
            print(bas,'
',tbas)
            cols = []
            for jj in range(len(bas)-1,0,-1):
                if cn>=bas[jj]:
                    print('cn=%s,jj=%s'%(cn,bas[jj]))
                    kk = (cn-bas[jj-1])//(26**jj)
                    cols.append(chr(ord('A')-1+kk))
                    cn -= kk* 26**jj
            cols.append(chr(ord('A')-1+cn))
            return ''.join(cols)

        def v2(columnNumber):
            cn= columnNumber
            res=[]
            #res = [chr((26 if cn%26==0 else cn%26)-1+ord("A"))]
            while cn - (26 if cn%26==0 else cn%26) >0:
                res.insert(0,chr((26 if cn%26==0 else cn%26)-1+ord("A")))
                cn= (cn- (26 if cn%26==0 else cn%26))//26
            res.insert(0,chr((26 if cn%26==0 else cn%26)-1+ord("A")))
            return ''.join(res)

