
A = int(input("Nilai a :"))
B = int(input("Nilai b :"))
C = int(input("Nilai c :"))
D = B**2-4*A*C
X = (-B+D/2)/2*A 
Y = (-B-D/2)/2*A
if D < 0 :
    print("Fungsi tersebut tidak memiliki akar rill")
elif D > 0 :
    print("Akar dari persamaan tersebut adalah", X,"dan", Y)
else :
    D == 0 
    print("Fungsi tersebut memiliki akar kembar yaitu", X)

