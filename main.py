var1 = "Python 2023"
var2 = "Python 2023"
var3 = var1

print(var1 == var2)
print(var2 == var3)






var1 = "Python 2023"
var2 = "Python 2023"
var3 = var1

print(type(var1), hex(id(var1)))
print(type(var2), hex(id(var2)))
print(type(var3), hex(id(var3)))






var3 = "Java 11"

print(var1 == var2)
print(var2 == var3)
print(type(var1), hex(id(var1)))
print(type(var2), hex(id(var2)))
print(type(var3), hex(id(var3)))







print("Kalkulator!")

liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))
operator = input("Wybierz operator (+, -, *, /): ")
if operator == "+":
    wynik = liczba1 + liczba2
    print(f"{liczba1} + {liczba2} = {wynik}")
elif operator == "-":
    wynik = liczba1 - liczba2
    print(f"{liczba1} - {liczba2} = {wynik}")
elif operator == "*":
    wynik = liczba1 * liczba2
    print(f"{liczba1} * {liczba2} = {wynik}")
elif operator == "/":
    wynik = liczba1 / liczba2
    print(f"{liczba1} / {liczba2} = {wynik}")
else:
    print("Nieznany operator.")



print("Ankieta!")
print("0.Jak masz na imię i nazwisko?")
print("")
name = input("Podaj imie i nazwisko: ")
print("1.Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
print("A)OGLĄDANIE TLEWIZJI/FILMÓW/SERIALI")
print("B)SŁUCHANIE MUZYKI")
print("C)PODRÓŻOWANIE")
odp1 = input("Podaj odpowiedź(DUŻA LITERA): ")
print("")
print("2.W jakich okolicznościach czytasz książki najczęściej?:")
print("A)PODCZAS PODRÓŻY")
print("B)W CZASIE WOLNYM")
print("C)W OGÓLE NIE CZYTAM")
odp2 = input("Podaj odpowiedź: ")
print("")
print("3.Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")
print("A)CHĘĆ POSZERZANIA WIEDZY")
print("B)CZYTANIE MNIE RELAKSUJE")
print("C)FAKT, ŻE CZYTANIE JEST MODNE")
odp3 = input("Podaj odpowiedź: ")
print("")



print("pytanie: Jak masz na imię i nazwisko?")
print(name)
print("pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
if odp1 == "A":
    print("odpowiedź: OGLĄDANIE TLEWIZJI/FILMÓW/SERIALI")
elif odp1 == "B":
    print("odpowiedź: SŁUCHANIE MUZYKI")
elif odp1 == "C":
    print("odpowiedź: PODRÓŻOWANIE")


print("pytanie: W jakich okolicznościach czytasz książki najczęściej?")
if odp2 == "A":
    print("odpowiedź: PODCZAS PODRÓŻY")
elif odp2 == "B":
    print("odpowiedź: W CZASIE WOLNYM")
elif odp2 == "C":
    print("odpowiedź: W OGÓLE NIE CZYTAM")


print("pytanie: Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")
if odp3 == "A":
    print("odpowiedź: CHĘĆ POSZERZANIA WIEDZY")
elif odp3 == "B":
    print("odpowiedź: CZYTANIE MNIE RELAKSUJE")
elif odp3 == "C":
    print("odpowiedź: FAKT, ŻE CZYTANIE JEST MODNE")
