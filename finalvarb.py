def command1(n1): #defining a function
    if n1%2==0: #checking whether when the number is divided by 2 does it give a remainder 0
        print("It is an even number") #it gives a remainder 0 
    else:
        print("It is an odd number") #it does not give a remainder 0
def command2(n1): #defining a function
    if n1>0: #checking whether the number is greater than 0
        print("It is a positive number") #it is greater than 0
    else:
        print("It is a negative number") #it is less than 0
def command3(n1): #defining a function
    print(n1*n1) #print the square of the given number
def command4(n1): #defining a function
    print(n1*n1*n1) #print the cube of the given number

def main():
    n=int(input('Enter Number: '))
    command1(n) #calling the function command1
    command2(n) #calling the function command2
    command3(n) #calling the function command3
    command4(n) #calling the function command4
main()