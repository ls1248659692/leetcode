class Solution:
    def intToRoman(self, num: int) -> str:
        p3=num//1000
        r3 ={1:'M',2:'MM',3:'MMM'}.get(p3,'')
        p2 = (num%1000 //100)
        r2 ={1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}.get(p2,'')
        p1 = (num%100 //10)
        r1 ={1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}.get(p1,'')
        p0 = num%10
        r0 ={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}.get(p0,'')                
        return r3 + r2 + r1 + r0