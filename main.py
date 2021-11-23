from cyk import *
v, t = bacaGrammar('chowsky')
r = 'forvinrange(13):continue'
ta = cyk(v, t, r)
tunjukkanHasil(ta, r)