class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)
        for i in range(len(sensor1)):
            if sensor1[i] != sensor2[i]:
                n = i
                break
        if n >= len(sensor1) - 1:
            return -1
        if sensor1[n:-1] == sensor2[n + 1:]:
            if sensor2[n:-1] == sensor1[n + 1:]:
                return -1
            return 1
        return 2
