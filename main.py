from cyk import *
from utils import *

v, t = bacaGrammar('chowsky')

r = bacaFile('tc1.txt')

print(r)
if len(r) == 0:
    print("Cocok dengan grammar !")
else:
    ta = cyk(v, t, r)
    tunjukkanHasil(ta, r)