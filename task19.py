text = "salom dunyo"
c = 0

for harf in text.lower():
    if harf in "aeiou":
       c += 1

print(c)