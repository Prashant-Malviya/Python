def avg():
    a = int(input('enter your number: '))
    b = int(input('enter your number: '))
    c = int(input('enter your number: '))

    average = (a+b+c)/3
    print(average)
    

# avg()

n = int(input('enter a number: ' ))

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

fact = factorial(5)

print(fact)