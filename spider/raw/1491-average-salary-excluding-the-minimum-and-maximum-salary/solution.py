class Solution:
    def average(self, salary: List[int]) -> float:
        su,mi,mx=0,10**7,0
        for s in salary: su,mi,mx= su+s, min(s,mi),max(s,mx)
        return (su-mi-mx)/(len(salary)-2)