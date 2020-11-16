string = "Th!s Sh0uLd B3 uPp3rCas3!"
print(string.upper())

fname = input("Enter file name: ")
fh = open(fname)
valores = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    print(line)
print("Done")






file = input("Enter file name: ")
abra = open(file)
value = 0
div = 0
for line in file:
    print('1')
    if line.startswith("Received"):
        numb = line.find(' ')
        print('2')
        print(numb)
print('done')

valo = line[numb:]
print(valo)