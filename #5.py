n = input("Masukkan nilai : ")
n = int(n)
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()