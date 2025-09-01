n1 = float(input("Enter number 1:"))
n2 = float(input("Enter number 2:"))

a  = print("Choose operator: * , / , + , -")
op = input("Enter operator:")

if op == "*" :
    print("Ans:",n1*n2)
elif op == "-" :
    print("Ans:",n1-n2) 
elif op == "+" :
    print("Ans:",n1+n2)
elif op == "/" :
    if n2 != 0:
        print("Ans:",n1/n2)
    else:
        print("Error!")        

else:
    print("Invalid Operator!")