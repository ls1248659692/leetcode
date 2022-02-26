# filter None return True object
def findLeftMostNode(root):
    queue = [root]
    for node in queue:
        queue += filter(None, (node.right, node.left))
    return node.val


# Sentinel
from functools import reduce
def permute_unique(nums):
    return reduce(lambda perms, n: [p[:i] + [n] + p[i:] for p in perms for i in range((p + [n]).index(n) + 1)], nums, [[]])


# assignment on the fly
# Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# Because it's not fully sorted, we can't do normal binary search. But here comes the trick:
#
# If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
# [12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
#
# If target is let's say 7, then we adjust nums to this:
# [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# And then we can simply do ordinary binary search.
#
# Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at. And the adjustment is done by comparing both the target and the actual element against nums[0].
def search(self, nums: 'List[int]', target: int) -> int:
    L, H = 0, len(nums)
    while L < H:
        M = (L + H) // 2
        if target < nums[0] < nums[M]:  # -inf
            L = M + 1
        elif target >= nums[0] > nums[M]:  # +inf
            H = M
        elif nums[M] < target:
            L = M + 1
        elif nums[M] > target:
            H = M
        else:
            return M
    return -1


def search(self, nums, target):
    lo, hi, t = 0, len(nums) - 1, (target < nums[0], target)
    while lo <= hi:
        mid = (lo + hi) // 2
        guess = (nums[mid] < nums[0], nums[mid])
        if guess == t:
            return mid
        elif guess < t:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1