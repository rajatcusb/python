def calculator(n1,n2,operator):
    if operator=='+':
        result=n1+n2
    elif operator=='-':
        result=n1-n2
    elif operator=='*':
        result=n1*n2
    elif operator=='/':
        result=n1/n2
    elif operator=='^':
        result=n1**n2
    return result
number1=float(input('Enter first number: '))
operator=input('Enter operator (+,-,*,/,**): ')
number2=float(input('Enter second number: '))
result=calculator(number1,number2,operator)
print(result)
