class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def v0(a,b,c):
            def xyz2abc(ss,xx,yy,zz,a,b,c):
                ss=ss.replace('a','x').replace('b','y').replace('c','z')
                #sorted([[xx,'a'],[yy,'b'],[zz,'c']])
                lst = [ss.count(i)for i in ['x','y','z']]
                for k,v in zip(['x','y','z'],[e for e in sorted([(a,'a'),(b,'b'),(c,'c')])]): ss=ss.replace(k,v[1])
                   

                # if zz==a: ss= ss.replace('z','a')
                # if zz==b: ss= ss.replace('z','b')
                # if zz==c: ss= ss.replace('z','c')
                # if yy==a and 'a' not in ss: ss= ss.replace('y','a')
                # if yy==b and 'b' not in ss: ss= ss.replace('y','b')
                # if yy==c and 'c' not in ss: ss= ss.replace('y','c')
                # if xx==a and 'a' not in ss: ss= ss.replace('x','a')
                # if xx==b and 'b' not in ss: ss= ss.replace('x','b')
                # if xx==c and 'c' not in ss: ss= ss.replace('x','c')  
                return ss    

            if a==0 or b==0 or c==0:
                #b<c 1:4 2:2b+2
                xx,yy,zz= sorted([a,b,c])
                if yy==0: tli=[  'z'*min(2,zz) ] 
                else:
                    if zz-2>=2*yy:  tli= ['ccb']*yy + ['cc']      
                    elif zz-1==2*yy: tli= ['ccb']*yy + ['c']
                    else: 
                        tli= ['ccb']*(zz//2) +['c'*(zz%2)] 
                        tli = [tli[i]+('b' if i<yy-zz//2 else '' )for i in range(len(tli))]
                ss = ''.join(tli)
                return xyz2abc(ss,xx,yy,zz,a,b,c)
            else:    
                # a,b,c  2b<c 2(a+b)<c (cc[ab]){n,} +'cc' a+b . c//2
                xx,yy,zz= sorted([a,b,c])
                x,y,z= sorted([a,b,c])
                
                zmax = min(2*(xx+yy)+2,zz)
                tail = max(0,zmax-2*x-2*y)
                z =zmax -tail
                print(xx,yy,zz,'zmax,tail',zmax,tail,'xyz',x,y,z)
                if z >= 2*(x+y): 
                    tli= ['cca']*x+ ['ccb']*y
                else:
                    if z>=2*y:
                        tli = ['ccb']*y+['cca']*(z//2-y) +['c'*(z%2)] #after that, z=0 ,y=0
                        tli = [tli[i]+('a' if i <x-z//2+y else '')for i in range(len(tli))]
                    elif z<2*y:
                        tli = ['ccb']*(z//2)+['c'*(z%2)] # afther that z=0, y>0
                        tli = [tli[i]+('b' if i<y-z//2 else '' ) for i in range(len(tli))] # y=0
                        tli = [tli[i]+('a' if i<min(zz//2,x) else '') for i in range(len(tli))]
                        if x-zz//2>0:
                            tli = [tli[i]+('a' if i<(x-zz//2) else '') for i in range(len(tli) )]
                ss= ''.join(tli+ ['c'*tail])
                ss=ss.replace('a','x').replace('b','y').replace('c','z')
                print(ss)
                return xyz2abc(ss,xx,yy,zz,a,b,c)  
        return v0(a,b,c)

        def v1(a,b,c):
            def longestDiverseString(self, a: int, b: int, c: int) -> str:
                res = ''
                add_list = sorted([[a,'a'],[b,'b'],[c,'c']])
                while ( add_list[0][0] != 0 or add_list[1][0] != 0):
                    add_list = sorted([[add_list[0][0],add_list[0][1]],[add_list[1][0],add_list[1][1]],[add_list[2][0],add_list[2][1]]])
                    # [[1, 'a'], [1, 'b'], [7, 'c']]
                    if len(res) < 2 and add_list[-1][0] >= 1:
                        res = res + add_list[-1][1]
                        add_list[-1][0] = add_list[-1][0] - 1
                    elif len(res) >= 2 and 2*add_list[-1][1] != res[-2:]:
                        res = res + add_list[-1][1]
                        add_list[-1][0] = add_list[-1][0] - 1
                    elif len(res) >= 2 and 2 * add_list[-1][1] == res[-2:]:
                        res = res + add_list[-2][1]
                        add_list[-2][0] = add_list[-2][0] - 1
                add_list = sorted([[add_list[0][0],add_list[0][1]],[add_list[1][0],add_list[1][1]],[add_list[2][0],add_list[2][1]]])

                if add_list[2][0] >= 2:
                    res = res + 2 *add_list[2][1]
                if add_list[2][0] == 1:
                    res = res + 1 *add_list[2][1]
                return(res)

        # [[1, 'a'], [1, 'b'], [7, 'c']]
        def v1b(a,b,c):
            res,lst = '',sorted([[a,'a'],[b,'b'],[c,'c']],key=lambda xx:xx[0])
            addabc = lambda r,li: r+li[1],[li[0]-1,li[1]]
            while ( lst[0][0] or lst[1][0] ):
                lst = sorted(lst)
                if len(res) < 2 and lst[-1][0] >= 1:  
                    res,lst[-2] = addabc(res,lst[-1])
                elif len(res) >= 2:
                    i = -2 if  2 * lst[-1][1] == res[-2:] else -1
                    res,lst[i] = addabc(res,lst[i])
            lst = sorted(lst)
            res += (2 if lst[-1][0] >= 2 else lst[-1][0]) *lst[-1][1]
            return(res)

        return v1b(a,b,c)