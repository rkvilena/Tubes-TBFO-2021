def hilangkanKomentar(x):
  while('#' in x):
    indeksA = x.find('#')
    awal = x[:indeksA]
    akhir = x[indeksA:]
    if(';' in akhir):
      indeksB = akhir.find(';')
      x=awal + akhir[indeksB+1:]
    else:
      x=awal

  while("'''" in x):
    indeksA = x.find("'''")
    awal = x[:indeksA]
    akhir = x[indeksA+3:]
    if("'''" in akhir):
      indeksB = akhir.find("'''")
      x=awal + akhir[indeksB+3:]
    else:
      print("error !")

  while('"""' in x):
    indeksA = x.find('"""')
    awal = x[:indeksA]
    akhir = x[indeksA+3:]
    if('"""' in akhir):
      indeksB = akhir.find('"""')
      x=awal + akhir[indeksB+3:]
    else:
      print("error !")
    
  return x

def hilangkanIndent(x):
    if(len(x)!=0):
      while(x[0]=='~'):
          x=x[1:]

    if(';' in x):
        awal = x[:x.find(';')+1]
        akhir = x[x.find(';')+1:]
        return awal + hilangkanIndent(akhir)
    else:
        return x

def hilangkanEnter(x):
    while(len(x)!=0 and x[0]==';'):
        x=x[1:]
    while(len(x)!=0 and x[-1]==';'):
        x=x[:-1]
    return x

def bacaFile(x):
    with open(x, 'r') as file:
        r = file.read().replace('\n', ';').replace(' ','~')
    r = hilangkanKomentar(r)
    r = hilangkanIndent(r)
    r = hilangkanEnter(r)
    return r