class Solution:
    def capitalizeTitle(self, title: str) -> str:
        tli = title.split()
        return ' '.join([wd.lower() if len(wd)<=2 else wd[0].upper()+wd[1:].lower() for wd in tli])