from replit import clear
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

operations = {"+":add,"-":subtract,"*":multiply,"/":division}

def calculator():
    num1 = float(input("What is your first number:\n"))
    for i in operations:
        print(i)

    keepgoing = True

    while keepgoing:
        choose = input("Pick an operation\n")
        num2 = float(input("What is your second number:\n"))
        cal01 = operations[choose]
        answer = cal01(num1, num2)
        print(f"{num1}{choose}{num2}={answer}")
        keepgo = input("Type 'y' to continue, type 'n' to exit.\n")

        if keepgo =='y':
            num1 = answer

        elif keepgo =='n':
            keepgoing=False
            clear()
            calculator()

calculator()