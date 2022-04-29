class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area**0.5)+1,0,-1):
            if area %i==0: return [max(area//i,i),min(area//i,i)]
 