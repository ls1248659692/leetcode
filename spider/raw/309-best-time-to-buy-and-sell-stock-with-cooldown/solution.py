strit=lambda x: ' '.join(str(x.get(k,'.')) for k in 'pf si prevpf prevsi lowi'.split() )
MX,MI=float('inf'),float('-inf')
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def v1(pr):
            dp = [{'pf':0,'si':-99999,'prevpf':0,'prevsi':-99999,'lowi':0}]*len(pr) #prof,selli,previous_pf,previous_selli,lowi(cantrade_pr)
            for i in range(1,len(pr)):
                #print(pr[:i+1],'		'.join([strit(d) for d in dp[i-1:i]]))
                p,last= pr[i],dp[i-1]
                newbschg= p- pr[last['lowi']] if last.get('lowi',-1)>=0 else MI
                chg = p - pr[last['si']] if last['si']>=0 else MI
                prevchg = p-min(pr[last['prevsi']+2:i+1]) if last['prevsi']+2<i+1 and last['prevsi']+2<len(pr) else MI
                if newbschg>0:
                    dp[i]= {'pf':last['pf'] +p- pr[last['lowi']],'si':i,'prevsi':last['si'],'prevpf':last['pf']}
                elif i>=last['si']+2:
                    print('prevsi',p,prevchg,last,p-min(pr[last['si']+2:i+1]))
                    if prevchg>0 and last['prevpf']+prevchg >last['pf']+max(p-min(pr[last['si']+2:i+1]),max(chg,0)):
                        dp[i]= {'pf':last['prevpf']+prevchg,'si':i,'prevsi':last['si'],'prevpf':last['pf']}
                    elif last['pf']+max(chg,0)>last['pf']+p-min(pr[last['si']+2:i+1]):
                        dp[i]= {'pf':last['pf']+chg,'si':i,'prevsi':last['si'],'prevpf':last['pf']}
                    else:
                        dp[i]= {'pf':last['pf'],'si':last['si'],'prevsi':last['prevsi'],'prevpf':last['prevpf'],'lowi':i} 
                elif i==last['si']+1 and chg>0:
                    dp[i]= {'pf':last['pf']+chg,'si':i,'prevsi':last['si'],'prevpf':last['pf']}    
                else:                            
                    dp[i]= {'pf':last['pf'],'si':last['si'],'prevsi':last['prevsi'],'prevpf':last['prevpf']}
            return dp[-1]['pf']          
        return v1(prices)