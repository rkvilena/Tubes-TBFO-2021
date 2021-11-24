from cyk import *
from utils import *

v, t = bacaGrammar('chowsky')

r = bacaFile('testcase/tc6.py')

print(r)
if len(r) == 0:
    print("Cocok dengan grammar !")
else:
    ta = cyk(v, t, r)
    tunjukkanHasil(ta, r)