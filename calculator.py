print('WELCOME TO MY FIRST CALCULATOR!')

num1=float(input('Enter the first number : '))
num2=float(input('Enter the second number : '))

print('1.Addition (+)')
print('2.Subtraction (-)')
print('3.Multiplication (*)')
print('4.Division (/)')

op = (input('Enter your operation : '))

if  op=="+":
    result=num1+num2
    print('Result=',result)
elif  op=="-":
    result=num1-num2
    print('Result=',result)
elif  op=="*":
    result=num1*num2
    print('Result=',result)
elif  op=="/":
        if num2==0:
            print("Error")
        else :
            result=num1/num2
            print('Result=',result)
else:
    print('INVALID')