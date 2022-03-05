class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum( it[{'type':0,'color':1,'name':2}[ruleKey]]==ruleValue for it in items)