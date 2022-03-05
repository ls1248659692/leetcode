class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cd = {ch:chars.count(ch) for ch in set(list(chars))}
        res = [wd for wd in words if sum(1 for ch in set(list(wd)) if cd.get(ch,0)-wd.count(ch)<0)<=0]
        print(res)
        return sum(len(el) for el in res)