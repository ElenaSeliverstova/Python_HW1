# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = True
y = False
z = True

left = not(x or y or z)
right = not(x) and not(y) and not(z)

print(left == right)