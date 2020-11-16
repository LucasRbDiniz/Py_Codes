file = input("Enter file name: ")
abra = open(file)
count = 0
pos = 0
total = 0
for line in abra:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else :
        count = count + 1
        pos = line.find(':')
        res = line[pos+1 : ]
        total = total + float(res)
media = total/count
print("Average spam confidence:", media)