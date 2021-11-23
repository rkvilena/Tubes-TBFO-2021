from cyk import *
v, t = bacaGrammar('chowsky')
with open('tc1.txt', 'r') as file:
    r = file.read().replace('\n', ';').replace(' ','~')
#r='def~jun():;x=2'
print(r)

if len(r) == 0:
    print("Cocok dengan grammar !")
else:
    ta = cyk(v, t, r)
    tunjukkanHasil(ta, r)