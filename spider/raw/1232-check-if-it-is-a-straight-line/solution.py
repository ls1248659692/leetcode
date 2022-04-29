class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ans = []
        coordinates = sorted(coordinates, key=lambda x: (x[0], x[1]))
        for i in range(len(coordinates)-1):
            if coordinates[i+1][0] == coordinates[i][0]:
                ans.append('zero')
            else:
                ans.append((coordinates[i+1][1]-coordinates[i][1])/(coordinates[i+1][0]-coordinates[i][0]))
        return len(set(ans)) == 1