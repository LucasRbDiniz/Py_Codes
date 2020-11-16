text = "X-DSPAM-Confidence:    0.8475"
ache = text.find('0')
number = float(text[ache:])
print(number)