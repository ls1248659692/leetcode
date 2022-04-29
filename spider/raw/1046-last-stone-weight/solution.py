class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = sorted(stones,reverse=True)
        while len(st)>1:
            left = st[0]-st[1]
            print(st,left)
            st = st[2:]
            if left:
                if st:
                    if st[-1]>left:
                        st.append(left)
                    else:
                        for j in range(len(st)):
                            if st[j]<=left:
                                st.insert(j,left)
                                break
                else:
                    return left
        return st[0] if st else 0