# Bit manipulation is the act of algorithmically manipulating bits or other pieces of data shorter than a word.
#
# common bit-wise operation
#
# operations priority:
# {}[]() -> ** -> ~ -> -x -> *,/,% -> +,- -> <<,>> -> & -> ^ -> | -> <>!= -> is -> in -> not x -> and -> or


def bit_wise_operations(a, b):
    # not
    ~a

    # or
    a | b

    # and
    a & b

    # xor
    a ^ b

    # shift operators
    a << b
    a >> b

    # subtraction
    a & ~b

    # set bit, assign to 1
    a |= 1 << b

    # clear bit, assign to 0
    a &= ~(1 << b)

    # test bit
    if a & 1 << b: pass

    # extract last bit
    a & -a

    # remove last bit
    a & (a - 1)

    # check is odd or even
    if a & 1: print('odd')

    # clear right n bit
    a & (~0 << b)

    # clear left until to n
    a & ((1 << b) - 1)

# reference
# https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
