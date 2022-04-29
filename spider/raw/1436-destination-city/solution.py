class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return [en[1] for en in paths if en[1] not in [be[0] for be in paths]][0]