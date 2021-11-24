import os

def buatSel(awal, akhir):
    res = set()
    if awal == set() or akhir == set():
        return set()
    for f in awal:
        for s in akhir:
            res.add(f+' '+s)
    return res
    
def bacaGrammar(namaFile="./grammar.txt"):
    namaFile = os.path.join(os.curdir, namaFile)
    with open(namaFile) as grammar:
        rules = grammar.readlines()
        v_rules = []
        t_rules = []

        for rule in rules:
            left, right = rule.split(" -> ")
            right = right[:-1].split(" | ")
            for ri in right:
                if ri[0]=="'" and ri[-1]=="'":
                    t_rules.append([left, ri[1:-1]])
                else:
                    v_rules.append([left, ri.split(' ')])
        return v_rules, t_rules


def bacaInput(namaFile="./input.txt"):
    namaFile = os.path.join(os.curdir, namaFile)
    res = []
    with open(namaFile) as inp:
        inputs = inp.readlines()
        for i in inputs:

            # remove \n
            res.append(i[:-1])
    return res


def cyk(varies, terms, inp):
    length = len(inp)#
    var0 = [va[0] for va in varies]
    var1 = [va[1] for va in varies]
    table = [[set() for j in range(length-i)] for i in range(length)]
    for i in range(length):
        for te in terms:
            if inp[i] == te[1]:#
                table[0][i].add(te[0])
    for i in range(1, length):
        for j in range(length - i):
            for k in range(i):
                row = buatSel(table[k][j], table[i-k-1][j+k+1])
                #print(row)
                for ro in row:
                    #print(ro)
                    #print(var1)
                    for l in range(len(var1)):
                      if ro.split(' ') == var1[l]:
                        #print('ketemu!',var0[l])
                        table[i][j].add(var0[l])
    return table


def tunjukkanHasil(tab, inp):
    if 'S' in tab[len(inp)-1][0]:
        print("Accepted")
    else:
        print("Syntax Error")