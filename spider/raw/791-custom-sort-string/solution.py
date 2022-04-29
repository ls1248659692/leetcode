class Solution:
    def customSortString(self, order: str, s: str) -> str:
        do={order[i]:i for i in range(len(order))}
        return ''.join(list(sorted(list(s),key=lambda x:do.get(x,-1)))) 