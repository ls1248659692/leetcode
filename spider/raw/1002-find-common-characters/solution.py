class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
         wli = [[wd.count(ch)for ch in  [chr(ord('a')+i) for i in range(26)]]  for wd in words ]
         ali = [[chr(ord('a')+i)]*min([ww[i] for ww in wli] ) for i in range(26)]
         print (ali)
         
         return [el for rr in ali for el in rr]