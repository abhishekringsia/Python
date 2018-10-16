from itertools import permutations
from collections import Counter

input().rpartition(' ')
from collections import OrderedDict

n = int(input())
mydict = OrderedDict()
for _ in range(n):
    item, space, price = input().rpartition(' ')
    mydict[item] = mydict.get(item,0) + price
for item, price in mydict.items():
    print(" ".join([item, str(price)]))
