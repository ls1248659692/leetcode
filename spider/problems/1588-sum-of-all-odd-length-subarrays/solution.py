class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_get = 0
        for i in range(len(arr)):
            appear_time = (((i + 1) // 2) * ((len(arr) - i) // 2) + (i // 2 + 1) * ((len(arr) - i - 1) // 2 + 1))
            sum_get = appear_time * arr[i] + sum_get
        return sum_get