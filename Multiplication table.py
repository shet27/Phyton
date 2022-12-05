# using Nested for loop
num = int(input(" Please Enter any Positive Integer lessthan 10 : "))

print(" Multiplication Table ")

for i in range(num, 10):
    for j in range(1, 11):
        print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
    print('==============')
