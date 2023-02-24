#Zadanie1
n=20
for i in range(1,5):
    print(n*"*")
print()
#Zadanie2
for k in range(5):
    if k==0 or k==4:
        for l in range(1,20):
            print("*",end='')
    else:
        print("*                 *",end='')
    print()
print()
#Zadanie 3
m=1
for i in range(1,6):
    print(m*"*")
    m=m+1

#Zadanie4
x=(512-282)/((47*48)+5)
print(round(x,4))

#Zadanie5
for c in range(1,6):
    print(c*7,'---',end='')

print()
#Zadanie6

a="Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

print(a)
#Zadanie7


z=eval(input("Wprowadz 1 liczbe"))
w=eval(input("wprowadz 2 liczbe"))
print(z*w)

#Zadanie8

y=eval(input("Podaj wage w kilogramach"))
print("Waga w funtach to : ")
print(y*2.20462262)
