from cyk import *
from utils import *

v, t = bacaGrammar('chowsky')

with open('tc1.txt', 'r') as file:
    r = file.read().replace('\n', ';').replace(' ','~')


if len(r) == 0:
    print("Cocok dengan grammar !")
else:
    ta = cyk(v, t, r)
    tunjukkanHasil(ta, r)