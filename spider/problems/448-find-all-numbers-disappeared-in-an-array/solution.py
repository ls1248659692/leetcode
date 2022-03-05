class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nset = set(nums)
        return [i+1 for i in range(len(nums))if i+1 not in nset ]
            
        #a =  [ii+1 for ii in range(len(nums)) if ii+1 not in nums]
        #return a
        