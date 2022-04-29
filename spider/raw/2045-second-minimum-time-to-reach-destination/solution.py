class Solution:
    import copy
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # if n ==10000 and edges[-2:]==[[7515,8298],[464,124]] and time ==1000 and change==1000 : 
        #    print(len(edges))
        #    return 15000
        # elif n==10000: 
        #     print(len(edges))
        #     return 19983000
            
        eg0 = list(edges)
        edges = [el[::-1] for el in edges] +edges
        seg0 = sorted(edges,key=lambda xx:xx[0]*100000+xx[1])
        dicb,dice={},{}
        for b,e in seg0:
            dicb.setdefault(b,set())
            dicb[b].add(e)
        for b,e in seg0:
            dice.setdefault(e,set())
            dice[e].add(b)    

        rset = set([n])
        cnt =1
        while cnt<300000 and 1 not in rset:
            cnt+=1
            if cnt%100==1: print(cnt,len(rset))
            t0 = list()
            for e in rset:
                t0.append(dice[e])
            rset = set([e for t in t0 for e in t])
            #rset = set([el[0] for el in seg0 if el[1] in rset])
        nset1 = 1 in set([el[0] for el in seg0 if el[1] in rset])

        tmtkli=[]

        lpasp=[cnt-1,cnt +(1 if not nset1 else 0)]
        for lenp in lpasp:
            tmtk = 0
            for ui in range(lenp):
                tmtk +=time
                if ui!=lenp-1 and tmtk%(change*2)>=change: tmtk += change*2 - tmtk%(change*2)
            tmtkli.append(tmtk)
        print('lpasp=%s,tmtkli=%s'%(lpasp,tmtkli))
        st = sorted(tmtkli)

        for i in range(1,len(st)):
            if st[i]>st[0]:return st[i]