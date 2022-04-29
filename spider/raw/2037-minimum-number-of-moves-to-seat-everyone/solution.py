class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        se=sorted(seats)
        st=sorted(students)
        return sum(abs(se[i]-st[i]) for i in range(len(se)))
