def hitungtambah(a, b):
    hasil = a+b
    return hasil

def hitungkurang(a,b):
    hasil = a-b
    return hasil

a1=int(input("angka pertama: "))
a2=int(input("angka kedua: "))

hasiltambah = hitungtambah(a1, a2) #tanpa return di function hitungtambah, hasiltambah gatau valuenya apa
hasilkurang = hitungkurang(a1, a2) #tanpa return di function hitungkurang, hasilkurang gatau valuenya apa

print(hasiltambah)
print(hasilkurang)