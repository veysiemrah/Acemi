sayi=1
asalsayilar =[]

while True:
    sayi +=2
    bolen=2
    while True:
        if sayi % bolen == 0:
            break
        else:
            if bolen>sayi**0.5:
                print(sayi)
                asalsayilar.append(sayi)
                bolen +=1
                break
            else:
                bolen += 1
