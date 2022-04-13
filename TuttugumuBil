import random

x=random.randint(1,100)

print("1 ile 100 arasında bir sayı belirledim. Bilmeye çalış")

t=0
puan=100

while True:
    t= int(input("Tahminini yaz"))
    if puan <= 0:
        print("Sanırım oyunu anlamadın!!! Bence daha fazla uzatmayalım")
        print(f"Tuttuğum sayı: {x}")
        break
    elif t != x:
        puan -= 2
        if t>x:
            print("Belirlediğim sayı daha küçük")
        else:
            print("Belirlediğim sayı daha büyük")
    else:
        print("Tebrikler sayıyı buldun")
        print(f"Puanın: {puan}")
        break
