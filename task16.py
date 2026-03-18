chegirma = 100
sale = 0

yosh = int(input("yoshingiz: "))

if yosh < 7:
    sale = 50

if 7 <= yosh <= 17:
    sale = 20

if yosh >= 60:
    sale = 30

price = round(chegirma - chegirma * sale / 100)

print(f'yakuniy narx: {price} som ({sale}% chegrma qollanadi)')