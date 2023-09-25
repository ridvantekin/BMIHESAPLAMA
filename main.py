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
                        font=("Times New Roman", 16))
    sonuclariYaz.place(x=125, y=380)

def bmiHesapla():
    kilo = int(kiloGiris.get())
    boy = int(boyGiris.get())

    vki = kilo / (boy ** 2)
    formatted_tam_sayi = f"{vki:d}"
    sonuclariYaz.config(text=f"Vücut Kitle İndeksi: {vki}")











def hesaplaButonu():
    buton = tkinter.Button()
    buton.config(text="HESAPLAMA",
                 width=29,
                 height=4,
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