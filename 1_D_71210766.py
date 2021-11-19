
A = int(input("Harga makanan sebesar Rp"))
B = int(input("Harga snack sebesar RP"))
C = int(input("Harga minuman sebesar Rp"))
D = int(input("Uang yang anda bawa sebesar Rp"))

print("total yang harus anda bayar sebesar Rp",A+B+C)

if (D == A+B+C):
    print("Uang anda pas! Tidak ada kembalian dan utang :D")
elif (D < A+B+C):
    print("uang anda kuarang! Anda memiliki utang sebesar Rp",(A+B+C)-D)
else:
    (D > A+B+C)
    print("Anda memiliki kembalian sebesar Rp",D-(A+B+C))
