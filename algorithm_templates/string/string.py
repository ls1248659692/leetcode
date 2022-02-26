# string is traditionally a sequence of characters, either as a literal constant or as some kind of variable.
import string


def string_operations():
    s = 'abcab'

    # join
    ','.join(s)

    # split
    s.split(',')

    # replace
    s.replace()

    # index & find, index return -1 if not found
    s.index('a')
    s.find('a')
    s.rfind('a')

    # count
    s.count('a')

    # start & end with
    s.startswith('a')
    s.endswith('b')

    # translate
    intab = "aeiou"
    outtab = "12345"
    trantab = str.maketrans(intab, outtab)
    s.translate(trantab)

    # strip
    s.lstrip()
    s.rstrip()
    s.strip()

    # just
    s.ljust(10)
    s.rjust(10)
    s.center(10)
    s.zfill(10)

    # common string
    string.punctuation
    string.whitespace
    string.ascii_lowercase
    string.hexdigits
    string.printable