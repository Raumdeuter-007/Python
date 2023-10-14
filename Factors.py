
while True:
    try:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        break
    except ValueError:
        print("Wrong input entered")

HCF = 1
for i in range(1,number_1):
    if (number_1 % i == 0 and number_2 % i == 0):
        HCF = i
    
LCM = number_1 * number_2 // HCF
print("The HCF of the two numbers is: ", HCF)
print("The LCM of the two numbers is: ", LCM)