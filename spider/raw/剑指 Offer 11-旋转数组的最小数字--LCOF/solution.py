class Solution:
    def minArray(self, numbers: List[int]) -> int:
        for i in range(1,len(numbers)):
            if numbers[i]<numbers[i-1]:return numbers[i]
        return numbers[0]