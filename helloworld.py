class ClassAsal :
    def asalSayilariBul(self, sayi1, sayi2):  
     for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

if __name__== '__main__':
    print("Asal Sayilar")
    sayi1 = int(input('sayi 1:'))
    sayi2 = int(input('sayi 2:'))
    p1 = ClassAsal()

    p1.asalSayilariBul(sayi1, sayi2)
