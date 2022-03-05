class Trie:

    def __init__(self):
        self.wset=set()
        self.abdic=dict()


    def insert(self, word: str) -> None:
        self.wset.add(word)
        self.abdic.setdefault(word[0],{})
        if len(word)>1:
            self.abdic[word[0]].setdefault(word[1],[])
            self.abdic[word[0]][word[1]].append(word)
        else:
            self.abdic[word[0]].setdefault(word,{})

    def search(self, word: str) -> bool:
        return word in self.wset


    def startsWith(self, prefix: str) -> bool:
        if len(prefix)==1: return prefix in self.abdic
        elif len(prefix)==2: return prefix[0] in self.abdic and prefix[1] in self.abdic[prefix[0]]
        else:
            if prefix[0] in self.abdic and prefix[1] in self.abdic[prefix[0]]:
                for wd in self.abdic[prefix[0]][prefix[1]]:
                    if len(prefix)<=len(wd) and wd[:len(prefix)]==prefix:return True
            return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)