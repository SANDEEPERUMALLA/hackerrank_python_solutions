from __future__ import print_function
from itertools import groupby

string = input()
for key, group in groupby(string):
    print((len(list(group)), int(key)), end=" ")
