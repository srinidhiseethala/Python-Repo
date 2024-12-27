n=int(input())
a=list(map(int,input().split()))
c=0
def isprime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
for i in a:
    if isprime(i):
        c+=1
print(c)