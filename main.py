import tkinter


def arayuz():

    arayuz = tkinter.Tk()
    arayuz.config(bg="#fbba0b")
    arayuz.wm_minsize(450,500)
    arayuz.title("BMI HESAPLAMA UYGULAMASI")



def kiloLabel():
    kiloMetni = tkinter.Label(bg="#fbba0b",
                              text="Lütfen Kilonuzu Giriniz",
                              font=("Times New Roman",16))
    kiloMetni.place(x=125, y=60)

def kiloEntry():
    global kiloGiris
    kiloGiris = tkinter.Entry()
    kiloGiris.config(width=20,                      #genişlik
                     bd=5,                          #çerçeve kalınlığı
                     fg="dark blue",                #yazı rengi
                     justify="center",              #yazı merkezi
                     bg="white",                    #arkaplan rengi
                     font=("Times New Roman",15))   #yazı font ve kalınlığı
    kiloGiris.focus()                               #imlecin ilk nerede başlayacağı
    kiloGiris.place(x= 125,y= 90)
    

def boyLabel():
    boyMetni = tkinter.Label(bg="#fbba0b",
                             text="Lütfen Boyunuzu Giriniz",
                             font=("Times New Roman", 16))
    boyMetni.place(x=125, y=150)

def boyEntry():
    global boyGiris
    boyGiris = tkinter.Entry()
    boyGiris.config(width=20,                            #genişlik
                    bd=5,                                #çerçeve kalınlığı
                    fg="dark blue",                      #yazı rengi
                    justify="center",                    #yazı merkezi
                    bg="white",                          #arkaplan rengi
                    font=("Times New Roman", 15))        #yazı font ve kalınlığı

    boyGiris.place(x=125, y=180)



def sonucMetni():
    global sonuclariYaz
    sonuclariYaz = tkinter.Label()
    sonuclariYaz.config(bg="#fbba0b",
                        font=("Times New Roman", 16, "bold"))
    sonuclariYaz.place(x=110, y=380)

def bmiHesapla():
    try:
        kilo = float(kiloGiris.get()) #girilen değer nokta ile girilmeli
        boy = float(boyGiris.get()) #girilen değer nokta ile girilmeli

    except ValueError: #hata mesajı
        sonuclariYaz.config(text="Lütfen Geçerli Bir Değer Giriniz")



    vki = kilo / (boy ** 2)



    if 10 < vki < 18:
        sonuclariYaz.config(text=f"Vücut Kitle İndeksi: {vki:.2f}\n Sonuç: Zayıf")
    elif 18 < vki < 25:
        sonuclariYaz.config(text=f"Vücut Kitle İndeksi: {vki:.2f}\n  Sonuç: Sağlıklı")
    elif 25 < vki < 30:
        sonuclariYaz.config(text=f"Vücut Kitle İndeksi: {vki:.2f}\n  Sonuç: Kilolu")
    elif 30 < vki < 40:
        sonuclariYaz.config(text=f"Vücut Kitle İndeksi: {vki:.2f}\n  Sonuç: Şişman")
    elif 40 < vki < 60:
        sonuclariYaz.config(text=f"Vücut Kitle İndeksi: {vki:.2f}\n  Sonuç: Obezite")





def hesaplaButonu():
    buton = tkinter.Button()
    buton.config(text="HESAPLAMA",
                 width=29,
                 height=4,
                 fg="black",
                 font=("calibri", 10, "bold"),
                 bg="#c8a2c8",
                 command=bmiHesapla)

    buton.place(x=125, y=250)


arayuz()
kiloEntry()
boyEntry()
kiloLabel()
boyLabel()
hesaplaButonu()
sonucMetni()

tkinter.mainloop()