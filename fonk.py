def selamla():
    print("Merhaba")
def topla(s1, s2):
    print("Toplam =", (s1 + s2))
def adsor():
    ad = input("Adınızı girin:")
    return ad 
def faktoryel(sayi):
    f = 1
    for i in range(1, sayi + 1):
        f = f * i
    return f

print("Ana Blok")
selamla() #parametre yok, dönen dğer yok
topla(5, 6) #parametre var, dönen değer yok
isim = adsor() #parametre yok, dönen değer var
print("Adınız," , isim)
sonc = faktoryel(5) #parametre var, dönen değer var
print("Sonuç = ", sonc)

