fname = input("Enter file name: ")
fh = open(fname)
lst = list()
abc = []
flat_list = []

for line in fh:
    linha = line.split()
    abc.append(linha)

flatList = [item for elem in abc for item in elem]
a = sorted(flatList)
fim = list(dict.fromkeys(a))
print(fim)
