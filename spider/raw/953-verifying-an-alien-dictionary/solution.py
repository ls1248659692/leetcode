class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        new_words = []
        english = [i for i in 'abcdefghijklmnopqrstuvwxyz']
        if len(words) ==1:
            return True
        dic = dict(zip(order,english))
        for i in words:
            res = ''
            for k in i:
                res += str(dic.get(k))
            new_words.append(res)
        for i in range(len(words)-1):
            if new_words[i]>new_words[i+1]:
                return False
        return True