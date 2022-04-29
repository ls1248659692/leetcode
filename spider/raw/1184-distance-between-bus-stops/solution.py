class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        ans = sum(distance[destination: start])  if start > destination else sum(distance[start: destination])
        return min(ans, sum(distance)-ans)