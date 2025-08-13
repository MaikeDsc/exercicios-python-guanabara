#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.

a, b, c = map(float, input().split())
pi = 3.14159
atri = a*c/2
acir = pi*c**2
atra = ((a+b)*c)/2
aqua = b**2
aret = a*b

print(f'TRIANGULO: {atri:.3f}')
print(f'CIRCULO: {acir:.3f}')
print(f'TRAPEZIO: {atra:.3f}')
print(f'QUADRADO: {aqua:.3f}')
print(f'RETANGULO: {aret:.3f}')