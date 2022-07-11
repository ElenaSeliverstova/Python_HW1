# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


A = int(input('Введите X '))
B = int(input('Введите Y '))
C = int(input('Введите Z '))
x = A
y = B
z = C

bool XYZ = x == A and y == B and z == C
bool notXYZ != XYZ
bool notXnotYnotZ = x != A and y != B and z != C

if (notXYZ == notXnotYnotZ):
    print("Утвеждение истинно")
else:
    print("Утверждение ложно")
