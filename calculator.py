import os

def main():
    os.system('CLS') #Clear Screen

    #welcome screen
    print ("Welcome to Calculator Ecek Ecek")
    print ("Ketik (1) kalau mau penambahan")
    print ("Ketik (2) kalau mau pengurangan")

    global inputOrang
    inputOrang = 0

    #------------------ FUNCTION ULANG --------------------------------------------
    def mauUlang():
        print ("Apakah mau mengulang?")
        print ("KETIK (1) untuk YA")
        print ("KETIK (2) untuk NO")
        userInput = input()
        if userInput == "1":
            main()
        elif userInput == "2":
            print ("Thank you!")
            os.system('CLS')
        else:
            mauUlang()

    #------------------ FUNCTION KALKULATOR --------------------------------------------
    def pilihProses():
        global inputOrang
        inputOrang = input("") #suruh orang pilih mau tambah/kurang/bagi/kali

        #------------------ FUNCTION OPERASI --------------------------------------------
        #PENAMBAHAN
        if int(inputOrang) == 1:
            listAngka = []
            
            print("Masukan angka-angka yang mau kalian tambahkan, ")
            print("ketik (0) kalau sudah selesai!")
            def processAngka():
                angkaInput = 1
                while int(angkaInput) != 0:
                    angkaInput = input("")
                    listAngka.append(int(angkaInput))
                
                #HITUNG DAN PRINT HASIL
                angkaHasil = sum(listAngka)
                print ("Hasil: " + str(angkaHasil))
                mauUlang()

            processAngka()
        
        #PENGURANGAN
        elif int(inputOrang)  == 2:
            print("Masukan angka-angka yang mau kalian tambahkan, ")
            print("ketik (0) kalau sudah selesai!")

        #ERRORLOG
        else:
            pilihProses()

    pilihProses()

main()