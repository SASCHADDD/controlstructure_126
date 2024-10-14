bilangan = int(input("Berapa banyak langkah? "))
n1, n2 = 0, 1
count = 0

if bilangan <= 0:
    print ("Harap masukkan nilai positif")
elif bilangan == 1:
    print ("Urutan fibonacci hingga",bilangan,":")
    print(n1)
else:
    print("ururtan fibonacci :")
    while count < bilangan:
        print (n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1