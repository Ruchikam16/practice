num1 =int(input("enter no 1\n"))
num2 =int(input("enter no 2\n"))

opt=input("enter the operation\n")

if opt =='Add':
    out=num1+num2
    print(out)

elif opt =='Subtract':
    out=num1-num2
    print(out)

elif opt=='Multiply':
    out=num1*num2
    print(out)

elif opt=='Divide':
    opt=num1/num2
    print(out)
