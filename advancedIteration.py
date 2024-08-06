list = [1, 2, 3, 4, 5, 6, 7, 8]

def twoBy():
    print ("PANJANG ELEMEN LIST:")
    print (len(list)) #BUAT CARI JUMLAH/PANJANG ELEMEN SUATU LIST
    print ("")

    listAngka = []
    for x in list: #-> Akan ngecek setiap elemen di list
        i = 0 #-> Setiap masuk elemen baru, i kita reset jadi 0

        while i<len(list): #-> Selama i lebih kecil dari panjang list:
            a = f'{x} {list[i]}'
            listAngka.append(a)
            print (a)
            i += 1
        print ("")
    print ("JUMLAH KOMBINASI:")
    print (len(listAngka))
    print ("")

def threeBy():
    listAngka = []
    for x in list:
        i = 0
        while i < len(list):
            y = 0
            while y < len(list):
                a = f'{x} {list[i]} {list[y]}'
                listAngka.append(a)
                print (a)
                y += 1
            i+= 1
            print ("")
        print ("")
    print ("JUMLAH KOMBINASI:")
    print (len(listAngka))

twoBy()
threeBy()