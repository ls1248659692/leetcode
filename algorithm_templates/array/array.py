# list is a collection which is ordered and changeable, with continuous space.
#
# Time:  O(1) to index or write or append, O(n) to insert or remove
# Space: O(n)


def list_operations():
    # initialization
    list1 = [3, 1, 2, 4]

    list2 = list(range(5))
    # [*X] equals to list(X)
    list2 = [*range(5)]

    # append
    list1.append(5)
    list1 += [5]
    list1 += 5,
    list1.extend([5, 6])

    # insert
    list1.insert(0)

    # index
    list1.index(3)

    # count
    list1.count(3)

    # remove
    list1.remove(3)

    # sort
    list1.sort(reverse=True)

    # reverse
    list1.reverse()
