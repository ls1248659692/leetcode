class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic ={}
        for wd in strs:
            s_wd = ''.join(sorted(list(wd)))
            dic.setdefault(s_wd,[])
            dic[s_wd].append(wd)
        return list(dic.values())