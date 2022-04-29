class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += int(count)
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]