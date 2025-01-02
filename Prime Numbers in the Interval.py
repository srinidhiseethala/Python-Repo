a=int(input())
b=int(input())
def isprime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

for i in range(a,b+1):
    if isprime(i):
        print(i)