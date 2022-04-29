class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        li = []
        for i in emails:
            a = i.split('@')
            a[0] = a[0].split('+')[0]
            a[0] = a[0].replace('.','')
            a = ' '.join(a)
            li.append(a)
        return len(set(li))