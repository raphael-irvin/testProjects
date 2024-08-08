#BASIC OOP
class Binatang:
    def __init__(self, habitat, constatus):
        self.habitat = habitat
        self.constatus = constatus
    
    def call(self):
        print("")
        print(f'Information Page'.upper())
        print(f'Habitat: {self.habitat}')
        print(f'Conservation Status: {self.constatus}')
        print("")

gajah = Binatang('Daratan', 'Langka')
anjing = Binatang('Daratan', 'Tidak Terancam')
pari = Binatang('Laut', 'Tidak Diketahui')

print (gajah.habitat) #-> Print habitat dari gajah
print (anjing.constatus) #-> Print constatus dari anjing
pari.call() #-> Call function call() dengan argument pari

#OOP FOR DATA
class ClassA1:
    def __init__(self, fullname, nickname, age, id):
        self.fullname = fullname
        self.nickname = nickname
        self.age = age
        self.studID = id
    
    def rollCall(self):
        print(f'Information for student {self.studID}:'.upper())
        print(f'Full Name: {self.fullname}')
        print(f'Nickname: {self.nickname}')
        print(f'Age: {self.age}')
        print("")

fullNames = ["Budi Satu", "Tono Dua", "Sutomo Tiga"]
nickNames = ["Budi", "Tono", "Sutomo"]
age = [18, 19, 20]

i = 0
for x in fullNames:
    x = ClassA1(x, nickNames[i], age[i], i)
    x.rollCall()
    i += 1

#OOP INHERITANCE
class dataOrang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def callInfo(self):
        print(f'Information for {self.nama}'.upper())
        print(f'Umur: {self.umur}')

class karyawan(dataOrang):
    def __init__(self, nama, umur, bidang):
        dataOrang.__init__(self, nama, umur)
        self.bidang = bidang

        dataOrang.callInfo(self)
        print(f'DATA TAMBAHAN: Bidang [{self.bidang}]')

user = karyawan('Agus', 17, 'IT')