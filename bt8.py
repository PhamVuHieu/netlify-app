def bai1(n):
    if n==1:
        return 4
    else:
        return 1/2*(bai1(n-1)+8)
for i in range (1,51):
    xdv=bai1(i)
    print(xdv)
def bai2(n):
    if n==1:
        return 5
    else:
        return 2-1/2+bai2(n-1)
for i in range (1,51):
    xdv=bai2(i)
    print(xdv)
    