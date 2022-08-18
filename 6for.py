#Caculate the factorial of a number

n = int(input("Enter anumber: "))

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(fact(n))



