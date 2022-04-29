class Solution:
    def decodeString(self, s: str) -> str:
        pstr = s.replace('[','(1.').replace(']','.1)')
        bli = []
        brac= ''
        print('pstr=%s'%pstr)
        for ii in range(len(pstr)):
            if pstr[ii]=='(':
                brac +='('
                bli.append([ii,brac])
            elif pstr[ii]==')':
                bli.append([ii,')'*len(brac)])
                brac = brac[:-1]
        pstr_li = list(pstr)
        maxbb = '('
        for pp,bb in bli:
            pstr_li[pp]=bb[0]
            pstr_li[pp +(1 if bb[0]=='(' else -1)]= str(len(bb))
            if len(bb)>=len(maxbb) and bb[0]=='(': maxbb= '(%d'%len(bb)
        pstr = ''.join(pstr_li)
        print('maxbb=%s,pstr=%s'%(maxbb,pstr))
        #return '()'
        if maxbb=='(':return pstr
        for mm in range(int(maxbb[1:]),0,-1):
            while '(%d.'%mm in pstr:
                tmpn =''
                pstr_p1,pstr_p2 ='',''
                tmpc=''
                lastn=0
                addc =False
                ii = 0
                while ii < len(pstr)-1:
                    if pstr[ii] in '0123456789' :
                            tmpn+=pstr[ii]
                    elif pstr[ii] !='(':
                        tmpn=''
                    if pstr[ii]=='(' and pstr[ii+1]==str(mm):
                        pstr_p1 = pstr[:ii-len(tmpn)]
                        lastn=int(tmpn)
                        tmpn=''
                        ii+=1
                        addc =True
                    elif pstr[ii]==str(mm) and pstr[ii+1]==')':
                        pstr_p2 = pstr[ii+1+1:]   
                        addc=False
                        break
                    else:
                        if addc and pstr[ii]!='.': tmpc+=pstr[ii] 
                    ii +=1
                n_pstr = pstr_p1 + lastn*tmpc + pstr_p2
                #print('pstr=%s,n_pstr=%s'%(pstr,n_pstr))
                pstr = n_pstr
                #break

        #pstr = ''.join(pstr_li)
        #print(bli,pstr)
        return pstr