class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        def abvsplit(s):
            r = [[s[0]]]
            for c in s[1:]:
                if c > r[-1][-1]:
                    r[-1].append(c)
                else:
                    r.append([c])
            return r        
        r =  abvsplit(nums)
        print(r)
        return max(len(sub) for sub in r)