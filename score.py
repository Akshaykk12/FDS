marks=[]
N=int(input("Enter the Number of students in the class: "))
print("Enter the Marks of the Students:")
for i in range(N):
    print(i+1,end=" ")
    m=int(input())
    marks.append(m)

def Average(marks,n):
    sum=0
    for i in marks:
        sum=sum+i
    avg= sum/n
    return avg

def Lowest(marks):
    lowest=marks[0]
    for i in marks:
        if lowest>i:
            lowest=i
        else:
            continue
    return lowest

def Highest(marks):
    highest=marks[0]
    for i in marks:
        if highest<i:
            highest=i
        else:
            continue
    return highest

def Absent(marks):
    count=0
    flag=0
    for i in marks:
        if i==0:
            flag=1
            count+=1
        else:
            continue
    if flag==0:
        print("There are no Absent students")
    else:
        print("The number of students who were Absent are:  ",count)

def Frequency(marks):
    max=0
    result=marks[0]
    for i in marks:
        freq=marks.count(i)
        if freq>max:
            max=freq
            result=i
    if max>1:
        return result
    else:
        return "Cannot Determine!"

while(True):
    print("Enter\n1-To Display Average score: ")
    print("2-Highest and Lowest score: ")
    print("3-Students Absent for the Exam: ")
    print("4-Display marks with Highest Frequency")
    print("0-Exit")
    ch=int(input("->"))
    if ch==1:
        a=Average(marks,N)
        print("The Average score is: ",a)
    elif ch==2:
        h=Highest(marks)
        print("The Highest marks of class :  ",h)
        l=Lowest(marks)
        print("The lowest score of Class is : ",l)
    elif ch==3:
        Absent(marks)
    elif ch==4:
        f=Frequency(marks)
        print("The marks with Highest frequency is: ",f)
    elif ch==0:
        break
    else:
        print("Choose given options only")