num1 = input("Masukkan nilai : ")
num2 = input("Masukkan nilai : ")
num3 = input("Masukkan nilai : ")

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
    
print("Nilai trbesarnya adalah : ",largest)