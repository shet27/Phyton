# program to find LCM 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm = num1 if(num1 > num2) else num2

while(True):
    if((lcm % num1 == 0) and (lcm % num2 == 0)):
        print("The L.C.M. of", num1,"and", num2,"is", lcm)  #LCM- least common multiple
        break
    lcm += 1
