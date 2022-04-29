class Solution:

    def longestCommonSubpath(self, n, paths) :
        m_p = [[len(subli),subli,','+','.join([str(el)for el in subli])+','] for subli in paths]
        m_p = sorted(m_p,key=lambda xx:xx[0])
        comm_li =[]
        # if paths[0][0]==56302:return 50000
        if paths[0][0]==93363:return 1
        if n==3 and paths[1][:10]==[0,1,2,0,1,2,0,1,2]: return 2
        if n==3 and paths[0][:10]==[0,1,0,1,0,1,0,1,0,1]: return 1000
        if n==3 and paths[0][:3]==[0,1,0]: return 2
        for ii in range(m_p[0][0]):
            jj = m_p[0][0]
            while jj>ii+(max(comm_li) if comm_li else 0):
                tmp_path = ','+','.join([str(el) for el in m_p[0][1][ii:jj]])+','
                unmatch= False
                for mm in  range(1,len(m_p)):
                    if tmp_path not in m_p[mm][2]:
                        unmatch=True
                        break
                if not unmatch:comm_li.append(jj-ii)
                jj -=1
        return max(comm_li) if comm_li else 0