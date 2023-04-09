i = 0
j=0
k = 0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
while True:
    print(f"{r}{q}{p}{o}{n}{m}{l}{k}{i}{j}")
    j+=1
    # print(f"{j}j")
    if r==9 and q==9 and p==9 and o==9 and n==9 and m==9 and l==9 and k==9 and i==9 and j==10:
        break
    if q==9 and p==9 and o==9 and n==9 and m==9 and l==9 and k==9 and i==9 and j==10:
        i=0
        j=0
        k=0
        l=0
        m=0
        n=0
        o=0
        p=0
        q=0
        r+=1
    elif p==9 and o==9 and n==9 and m==9 and l==9 and k==9 and i==9 and j==10:
        i=0
        j=0
        k=0
        l=0
        m=0
        n=0
        o=0
        p=0
        q+=1
    elif o==9 and n==9 and m==9 and l==9 and k==9 and i==9 and j==10:
        i=0
        j=0
        k=0
        l=0
        m=0
        n=0
        o=0
        p+=1
    elif n==9 and m==9 and l==9 and k==9 and i==9 and j==10:
        i=0
        j=0
        k=0
        l=0
        m=0
        n=0
        o+=1
    elif m==9 and l==9 and k==9 and i==9 and j==10:
        i=0
        j=0
        k=0
        l=0
        m=0
        n+=1
    elif l==9 and k==9 and i==9 and j==10:
        i=0
        j=0
        k=0
        l=0
        m+=1
    elif k==9 and i==9 and j==10:
        k=0
        i=0
        j=0
        l+=1
    elif i==9 and j==10:
        i=0
        j=0
        k+=1
    elif j==10:
        j=0
        i+=1
        # print(f"{i}i")
    else:
        pass