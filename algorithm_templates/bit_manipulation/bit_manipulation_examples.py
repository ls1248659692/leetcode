'''
baiscs
'''


# [191] https://leetcode.com/problems/number-of-1-bits/
# Write a function that takes an unsigned integer and return the number of '1' bits it has.
def hammingWeight(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count


# [342] https://leetcode.com/problems/power-of-four/
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# map-checking
def isPowerOfFour(num: 'int') -> 'bool':
    return num & (num - 1) == 0 and num & 0x55555555 != 0


'''
^ tricks
Use ^ to remove even exactly same numbers and save the odd, or save the distinct bits and remove the same.
'''


# [371] https://leetcode.com/problems/sum-of-two-integers/
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
def getSum(a, b):
    # 32 bits integer max
    MAX = 0x7FFFFFFF
    # 32 bits interger min
    MIN = 0x80000000
    # mask to get last 32 bits
    mask = 0xFFFFFFFF
    while b != 0:
        # ^ get different bits and & gets double 1s, << moves carry
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
    return a if a <= MAX else ~(a ^ mask)


# [268] https://leetcode.com/problems/missing-number/
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# bit manipulate,  a^b^b = a
def missingNumber(nums):
    res = 0
    for i, e in enumerate(nums):
        res = res ^ i ^ e
    return res ^ len(nums)


'''
| tricks
Keep as many 1-bits as possible
'''


# Find the largest power of 2 (most significant bit in binary form), which is less than or equal to the given number N.
def largest_power(n):
    # change all the right side bits to 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return (n + 1) >> 1


# [190] https://leetcode.com/problems/reverse-bits/
# Reverse bits of a given 32 bits unsigned integer.
def reverseBits1(n):
    mask, res = 1 << 31, 0
    for i in range(32):
        if n & 1:
            res |= mask
        mask >>= 1
        n >>= 1
    return res


def reverseBits2(n):
    mask, res = 1, 0
    for i in range(32):
        res <<= 1
        if mask & n:
            res |= 1
        mask <<= 1
    return res


'''
& tricks
Just selecting certain bits
'''


# Reversing the bits in integer
def reverse_bits(x):
    x = ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1)
    x = ((x & 0xcccccccc) >> 2) | ((x & 0x33333333) << 2)
    x = ((x & 0xf0f0f0f0) >> 4) | ((x & 0x0f0f0f0f) << 4)
    x = ((x & 0xff00ff00) >> 8) | ((x & 0x00ff00ff) << 8)
    return ((x & 0xffff0000) >> 16) | ((x & 0x0000ffff) << 16)


# [201] https://leetcode.com/problems/bitwise-and-of-numbers-range/submissions/
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
def rangeBitwiseAnd(m: int, n: int) -> int:
    count = 0
    while m != n:
        m >>= 1
        n >>= 1
        count += 1
    return m << count


'''
application
'''


# [187] https://leetcode.com/problems/repeated-dna-sequences/
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
def findRepeatedDnaSequences(s):
    res = []
    dic = {"A": 1, "C": 2, "G": 3, "T": 4}
    dicDNA = {}
    num = 1
    for i in range(len(s)):
        num = (num * 4 + dic[s[i]]) & 0XFFFFF
        if i < 9:
            continue
        if num not in dicDNA:
            dicDNA[num] = 1
        elif dicDNA[num] == 1:
            res.append(s[i - 9:i + 1])
            dicDNA[num] = 2
    return res


# [169] https://leetcode.com/problems/majority-element/
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# bit-counting as a usual way, but here we actually also can adopt sorting and Moore Voting Algorithm
def majorityElement(nums: 'List[int]') -> 'int':
    size = len(nums)
    mask = 1
    ret = 0
    for i in range(32):
        count = 0
        for j in range(size):
            if mask & nums[j]:
                count += 1
            if count > size // 2:
                ret |= mask
            mask <<= 1
    return ret


# [137] https://leetcode.com/problems/single-number-ii/
# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# bitwise operation for single problem
# https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
def singleNumber(nums: 'List[int]') -> 'List[int]':
    t, a, b = 0, 0, 0
    for num in nums:
        t = (a & ~b & ~num) | (~a & b & num)
        b = (~a & b & ~num) | (~a & ~b & num)
        a = t
    return a | b


# [318] https://leetcode.com/problems/maximum-product-of-word-lengths/
# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
def maxProduct(words: 'List[str]') -> int:
    max_len = 0
    word_bits = []
    for word in words:
        word_bit = 0
        for c in word:
            word_bit |= 1 << ord(c) - ord('a')

        for i, cur_bit in enumerate(word_bits):
            if cur_bit & word_bit == 0:
                max_len = max(max_len, len(words[i]) * len(word))

        word_bits.append(word_bit)
    return max_len


# [78] https://leetcode.com/problems/subsets/
# Given a set of distinct integers, nums, return all possible subsets (the power set).
def subsets(nums: 'List[int]') -> 'List[List[int]]':
    size = len(nums)
    num = 1 << size
    res = [[] for _ in range(num)]
    for i in range(num):
        for j in range(size):
            if (1 << j) & i:
                res[i].append(nums[j])
    return res
