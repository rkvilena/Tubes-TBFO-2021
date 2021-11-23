from cyk import *
v, t = bacaGrammar('chowsky')
r = 'v=(22+3)'
ta = cyk(v, t, r)
tunjukkanHasil(ta, r)