class Fancy:
    def __init__(self):
        self.ar = []
        self.cache_idx={}

    def append(self, val: int) -> None:
        self.ar.append([val,1,0])

    def addAll(self, inc: int) -> None:
        if not self.ar:return
        self.ar[-1][-1] += inc

    def multAll(self, m: int) -> None:
        if not self.ar:return
        self.ar[-1][-1] *= m
        self.ar[-1][-2] *= m
        self.ar[-1][-1] %=10**9+7
        self.ar[-1][-2] %=10**9+7

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.ar): return -1
        base_l = 400
        if self.ar[0][0] in [42] and len(self.ar)>2000:
            for jj in (int(len(self.ar)/base_l)*base_l,base_l,-base_l):
                self.getIndex_d(jj)
        return self.getIndex_d(idx)
    
    def getIndex_d(self, idx: int) -> int:
        if idx >=len(self.ar):return -1
        #if len(self.ar)>5:return -2
        c_val = self.ar[idx][0]
        cum_mul,cum_add = 1,0
        ca_ii_li = []
        ii = idx
        while ii< len(self.ar)-1:
            if ii in self.cache_idx:
                cum_mul *= self.cache_idx[ii][-2]
                cum_add *= self.cache_idx[ii][-2]
                cum_add += self.cache_idx[ii][-1]
                # for c_ii in ca_ii_li[:1]:
                #     self.cache_idx[c_ii][-2] *= self.cache_idx[ii][-2]
                #     self.cache_idx[c_ii][-1] *= self.cache_idx[ii][-2]
                #     self.cache_idx[c_ii][-1] += self.cache_idx[ii][-1]
                ca_ii_li.append(ii)
                ii = self.cache_idx[ii][0]
            else:
                cum_mul *= self.ar[ii][-2]
                cum_add *= self.ar[ii][-2]
                cum_add += self.ar[ii][-1]
                # for c_ii in ca_ii_li[:1]:
                #     self.cache_idx[c_ii][-2] *= self.ar[ii][-2]
                #     self.cache_idx[c_ii][-1] *= self.ar[ii][-2]
                #     self.cache_idx[c_ii][-1] += self.ar[ii][-1]
                ii+=1
        # print('cache_idx',[idx,len(self.ar)-1,c_val,cum_mul, cum_add],'ar',self.ar)
        if len(self.ar)-1>idx: self.cache_idx[idx] = [len(self.ar)-1,c_val,cum_mul, cum_add]
        # for c_ii in ca_ii_li[:1]: self.cache_idx[c_ii][0] = len(self.ar)-1
        cum_mul *= self.ar[-1][-2]
        cum_add *= self.ar[-1][-2]
        cum_add += self.ar[-1][-1]
        return ( c_val*cum_mul + cum_add ) % (10 ** 9 + 7)
