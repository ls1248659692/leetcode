class Solution:
    def simplifyPath(self, path: str) -> str:
        while '//'in path:path =path.replace(r'//',r'/')
        while path[-1]=='/' and len(path)>1:  path = path[:-1]
        pli = path.split('/')
        print('pli=%s'%pli)
        tli =[['*']]
        cur_depth = 0
        for ii in range(1,len(pli)):
            if pli[ii]=='.':
                pass
            elif pli[ii] == '..':
                if cur_depth>=1: cur_depth -=1
            else:
                cur_depth +=1
                if len(tli)<=cur_depth: tli.append([])
                tli[cur_depth].append(pli[ii])
        print('tli=%s,cur_depth=%s'%(tli,cur_depth))
        
        return '/'.join([el[-1] for el in tli[:cur_depth+1]])[1:] if cur_depth!=0 else '/'
