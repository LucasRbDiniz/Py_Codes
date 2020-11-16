def computepay(h,r):
    hora = float(h)
    taxs = float(r)
    if hora > 40:  # Hora extra
        cont = hora * taxs
        otmz = (hora - 40.0) * (taxs * 0.5)
        full = cont + otmz
    else:
        full = hora * taxs
    return full

hrs = input("Hours: ")
rate = input("Rate: ")
t = computepay(hrs,rate)
print("Pay:", t)
