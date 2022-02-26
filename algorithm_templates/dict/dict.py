# a data structure that implements an associative array abstract data type, a structure that can map keys to values
# variations: defaultdict, Counter, OrderedDict
#
# Time:  O(1)
# Space: O(n)
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from operator import itemgetter


def dict_operations():
    '''
    dict common operations
    '''
    # keys must be hashable (constant __hash__ and comparable via __eq__)
    # based on hash table -> O(1) for insertion, deletion, update, lookup

    # initialization
    dict1 = {'a': 2, 'b': 1, 'c': 1}

    # iteration
    for k, v in dict1.items():
        # check if key exists
        if k in dict1:
            # get and set
            dict1[k] = v + 1

    # get and set by default
    dict1.get('d', 0)
    dict1.setdefault('d', 0)

    # sorted by values
    sorted(dict1.items(), key=itemgetter(1))

    # pop value
    dict1.pop('a')

    '''
    default dict
    '''
    default_dict_list1 = defaultdict(int)
    default_dict_list1['e'] += 1

    default_dict_list2 = defaultdict(list)
    default_dict_list2['a'].append(1)

    '''
    Counter
    '''
    # count number, also a default dict
    counter = Counter(['a', 'b', 'a', 'c'])
    # unfold the elements
    counter.elements()
    # list the n most common elements
    counter.most_common(2)
    # update
    counter.update({'a': 1, 'b': 2})

    # add
    Counter('abbb') + Counter('bcc')
    # subtract, but keep only results with positive counts.
    Counter('abbb') - Counter('bcc')
    # union, the maximum of value in either of the input counters.
    Counter('abbb') | Counter('bcc')
    # intersection, the minimum of corresponding counts.
    Counter('abbb') & Counter('bcc')

    '''
    OrderedDict
    '''
    # key sorted in insert order, keys is a doubly linked list
    order_dict = OrderedDict(dict1)
    # update order to front or back
    order_dict.move_to_end('a', last=False)
