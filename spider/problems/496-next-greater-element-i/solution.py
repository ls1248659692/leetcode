class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [[e for e in nums2[nums2.index(n)+1:] if e>n][0] if [e for e in nums2[nums2.index(n)+1:] if e>n] else -1 for n in nums1]