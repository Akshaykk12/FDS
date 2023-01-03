m1=[]
m2=[]
size=int(input("Enter the size of the matrix: "))
print("Enter the Elements in the matrix: ")
for i in range(size):
    A=[]
    for j in range(size):
        a=int(input())   
        A.append(a)
    m1.append(A)
print("Enter the elements in second matrix: ")
for i in range(size):
    B=[]
    for j in range(size):
        b=int(input())
        B.append(b)
    m2.append(B)

def add():
    mat3=[]
    for i in range(len(m1)):
        ad=[]
        for j in range(len(m1[0])):
            ad.append(m1[i][j]+m2[i][j])
        mat3.append(ad)
    print("Addition of two matrices is")
    for i in mat3:
        print(i)

def subt():
    mat3=[]
    for i in range(len(m1)):
        sub=[]
        for j in range(len(m1[0])):
            sub.append(m1[i][j]-m2[i][j])
        mat3.append(sub)
    print("Subtraction of two matrices is")
    for i in mat3:
        print(i)

def product():
    pro=[]
    for i in range(size):
        A=[]
        for j in range(size):  
            A.append(0)
        pro.append(A)
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            for k in range(len(m1)):
                pro[i][j] += m1[i][k]*m2[k][j]
    print("Product of two matrices is")
    for i in pro:
        print(i)

def tran():
    pro=[]
    for i in range(size):
        A=[]
        for j in range(size):  
            A.append(0)
        pro.append(A)
    for i in range(size):
        for j in range(size):
            pro[i][j] = m1[j][i]
    print("Transpose of matrix is")
    for i in pro:
        print(i)

add()
subt()
product()
tran()