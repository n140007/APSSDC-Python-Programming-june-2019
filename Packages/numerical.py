# Series of N prime numbers

def isPrime(N):
    for i in range(2, N):
        count =0
        for j in range(1, i+1):
            if(i%j==0):
                count=count+1
        if(count==2):
            print(i, end = " ")
    return
N = int(input())
isPrime(N)




#squares of natural numbers
n = int(input())
def sumSquaresNaturalNumbers(n):
    sum=0
    for i in range(1, n+1):
        sum=sum+i**2
    return sum
sumSquaresNaturalNumbers(n)