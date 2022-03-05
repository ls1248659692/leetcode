class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for x, y in items:
            dic[x].append(y)
        ans = []
        for key, val in dic.items():
            tmp = sum(sorted(val)[::-1][:5]) // 5
            ans.append([key, tmp])
        ans.sort(key=lambda x: x[0])
        return ans
