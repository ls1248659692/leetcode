class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st,sw=students,sandwiches
        cnt=100000
        while st and cnt:
            #print(sw)
            cnt-=1
            if st[0]==sw[0]:
                del sw[0]
                del st[0]
            else:
                st=st[1:]+[st[0]]
        return len(st)
