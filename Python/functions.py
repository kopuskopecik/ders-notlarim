# returnden sonraki komutlar calismaz.
# herhangi bir deger dondurmeyen fonksiyonlara void fonksiyonlar denir.

def selamla(a:list[int]) -> str:
    return a

selamla('Elma')

def ikiyle_carp(a:int):
    return a * 2

print(ikiyle_carp(5))
print(ikiyle_carp(a=15))

# Default deger
def hello(name="Hany", age=12):
    print("Merhaba", name, age)

hello()
hello("Ahmet")
hello(age=15, name="Erdogan")

# * kullanimi - asagidaki ornekte a bir tupledir.
def toplama(*a):
    print(type(a), a)
    toplam = 0
    for i in a:
        toplam += i
    return toplam

print(toplama(1,2,3))

# ** kullanimi - asagidaki ornekte a bir sozluktur.
def carpma(**a):
    print(type(a), a)

print(carpma(erdogan='elma', hilmi='armut'))