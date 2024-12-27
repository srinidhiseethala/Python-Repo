n=int(input())
a=list(map(int,input().split()))
res=[]
def isprime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
for i in a:
    if isprime(i):
        res.append(i)
ans=sum(res)/len(res)
print(f"{ans:.2f}")