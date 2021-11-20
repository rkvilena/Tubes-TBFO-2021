import os


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
                if str.islower(ri):
                    t_rules.append([left, ri])
                else:
                    v_rules.append([left, ri])
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
    length = len(inp)
    var0 = [va[0] for va in varies]
    var1 = [va[1] for va in varies]
    table = [[set() for _ in range(length-i)] for i in range(length)]
    for i in range(length):
        for te in terms:
            if inp[i] == te[1]:
                table[0][i].add(te[0])
    for i in range(1, length):
        for j in range(length - i):
            for k in range(i):
                res = set()
                if table[k][j] == set() or table[i-k-1][j+k+1] == set():
                    return set()
                for f in table[k][j]:
                    for s in table[i-k-1][j+k+1]:
                        res.add(f+s)
                row = res
                for ro in row:
                    if ro in var1:
                        table[i][j].add(var0[var1.index(ro)])
    return table


def tunjukkanHasil(tab, inp):
    for c in inp:
        print("\t{}".format(c), end="\t")
    print()
    for i in range(len(inp)):
        print(i+1, end="")
        for c in tab[i]:
            if c == set():
                print("\t{}".format("_"), end="\t")
            else:
                print("\t{}".format(c), end=" ")
        print()

    if 'S' in tab[len(inp)-1][0]:
        print("Cocok dengan grammar !")
    else:
        print("Tidak cocok dengan grammar !")


if __name__ == '__main__':
    v, t = bacaGrammar()
    r = bacaInput()[0]
    ta = cyk(v, t, r)
    tunjukkanHasil(ta, r)