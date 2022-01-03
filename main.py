def function(x):
    return x**3 - 6*(x**2) + 20
def functionsh(x):
    return 3*x**2 - 12*x
def functionsh2(x):
    return 6*(x-2)

a = 2
b = 3

x = 2
fA = function(a)
fB = function(b)
fX = function(x)
fshA = functionsh(a)
fshB = functionsh(b)
fsh2A = functionsh2(a)
fsh2B = functionsh2(b)

e = float(input("Введите погрешность.\n"))

for i in range (0,6):
    if abs(fA) < e:
        print(i)
        print(f"x : {a}")
        print(f"f(x): {fA}")
        break
    if abs(fB) < e:
        print(i)
        print(f"x : {b}")
        print(f"f(x): {fB}")
        break
    if fA*fsh2A < 0:
        a = a - fA*(a-b)/(fA-fB)
        fA = function(a)
        fshA = functionsh(a)
        fsh2A = functionsh2(a)
    elif fA*fsh2A > 0:
        a = a - fA/fshA
        fA = function(a)
        fshA = functionsh(a)
        fsh2A = functionsh2(a)
    if fB*fsh2B < 0:
        b = b - fB*(b-a)/(fB-fA)
        fB = function(b)
        fshB = functionsh(b)
        fsh2B = functionsh2(b)
    elif fB*fsh2B > 0:
        b = b - fB/fshB
        fB = function(b)
        fshB = functionsh(b)
        fsh2B = functionsh2(b)
    print(i)
    print(f"a : {a}")
    print(f"b: {b}")
    print(f"f(x): {fB}")
    print("")