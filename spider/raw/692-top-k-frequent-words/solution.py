class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [el[0] for el in sorted({wd:words.count(wd) for wd in set(words)}.items(),key=lambda xx:str(99999-xx[1])+xx[0],reverse=False)][:k]
        dic = {wd:words.count(wd) for wd in set(words)}
        srt = sorted(dic.items(),key=lambda xx:str(99999-xx[1])+xx[0],reverse=False)
        return [el[0] for el in srt][:k]