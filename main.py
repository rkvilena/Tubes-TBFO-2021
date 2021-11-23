from cyk import *
v, t = bacaGrammar('chowsky')
r = 'for~v~in~range(2):;v=2'
ta = cyk(v, t, r)
tunjukkanHasil(ta, r)