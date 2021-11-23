import os

def create_cell(first, second):
    """
    creates set of string from concatenation of each character in first
    to each character in second
    :param first: first set of characters
    :param second: second set of characters
    :return: set of desired values
    """
    res = set()
    if first == set() or second == set():
        return set()
    for f in first:
        for s in second:
            res.add(f+s)
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
                row = create_cell(table[k][j], table[i-k-1][j+k+1])
                for ro in row:
                    if ro in var1:
                        table[i][j].add(var0[var1.index(ro)])
    return table


def tunjukkanHasil(tab, inp):
    print('masuk')
    print(type(tab))
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