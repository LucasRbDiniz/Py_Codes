lown = None
for n in [7,14,32,20,931,14,2,512]:
    if lown is None:
        lown = n
    elif n < lown:
        lown = n
print("Menor número é :", lown)