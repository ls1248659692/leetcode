class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ns = set(list(nums1)).intersection(set(list(nums2)))
        tli = [ [n]*min(nums1.count(n),nums2.count(n)) for n in ns]
        return [e for rr in tli for e in rr]