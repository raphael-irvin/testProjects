list = [1, 2, 3, 4, 5, 6, 7, 8]
print ("PANJANG ELEMEN LIST:")
print (len(list)) #BUAT CARI JUMLAH/PANJANG ELEMEN SUATU LIST
print ("")

for x in list: #-> Akan ngecek setiap elemen di list
    i = 0 #-> Setiap masuk elemen baru, i kita reset jadi 0

    while i<len(list): #-> Selama i lebih kecil dari panjang list:
        print (f'{str(x)} {str(list[i])}')
        i += 1
    print ("")