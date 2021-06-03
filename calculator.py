def addition(num1,num2):
    return num1+num2
    
def subtraction(num1,num2):
    return num1-num2

if __name__=="__main__":
    print("enter two numbers")
    num1=int(input())
    num2=int(input())
    print("Sum of two number is",addition(num1,num2))
    print("difference of two numbers is",subtraction(num1,num2))
