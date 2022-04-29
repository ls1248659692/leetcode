class Solution:
    def findLucky(self, arr: List[int]) -> int:
        list1= []
        for i in list(set(arr)):
            if i == arr.count(i):
                list1.append(i)
        return max(list1) if len(list1) >= 1 else -1