class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a= [chr(ord('a')+i) for i in range(26)]
        d= dict(zip(a,m))
        return len(set([''.join([d[ch] for ch in word]) for word in words]))