class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        cset = set(list1).intersection(set(list2))
        ri = [(rr,list1.index(rr)+list2.index(rr)) for rr in cset]
        min_id = min([el[1] for el in ri])
        return [el[0] for el in ri if el[1]==min_id]