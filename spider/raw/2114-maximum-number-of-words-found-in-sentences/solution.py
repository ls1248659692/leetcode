class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
         return max(len([el for el in st.strip().split(' ') if el]) for st in sentences)