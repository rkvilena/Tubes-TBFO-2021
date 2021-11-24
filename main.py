from cyk import *
from utils import *

v, t = bacaGrammar('chowsky')

x=input("Masukkan nama file yang ingin dicek syntaxnya (contohnya tc1.txt) : ")

r = bacaFile(x)

if len(r) == 0:
    print("Accepted")
else:
    ta = cyk(v, t, r)
    tunjukkanHasil(ta, r)