from cyk import *
v, t = bacaGrammar('chowsky')
with open('tc1.txt', 'r') as file:
    r = file.read().replace('\n', ';').replace(' ','~')
ta = cyk(v, t, r)
tunjukkanHasil(ta, r)