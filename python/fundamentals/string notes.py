from nose.tools import assert_equal, assert_true, assert_false
import sys
assert_equal(sys.version_info.major, 3)
import statistics
def olympic_average(els):
    if len(els) == 0:
        return None
    x = sum(els) / len(els)
    print (x)
    y = x % 1
    x = x - y
    if y < 0.25:
        return x
    elif y > 0.24 and y < 0.74:
        y = 0.5
        x += y
        return x
    elif y > 0.74:
        y = 1
        x += y
        return x

assert_equal(olympic_average([5, 3, 4, 5]), 4.5)
assert_equal(olympic_average([5, 6, 3, 4, 10]), 5)