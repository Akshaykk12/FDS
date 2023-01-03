sentence=input("Enter the Sentence:")
sen=sentence.split()
print(sen)
choice=1
while(choice!=0):
    print("1.Palindrome\n2.Index of sub string\n3.Frequency Occurance of each word.\n4.Exit\n")
    choice=int(input("Enter your Choice:"))
    if choice==1:
        sub=input("Enter the Sub String:")
        if sub==sub[::-1]:
            print(f"{sub} is Palindrome. \n")
        else:
            print(f"{sub} is not Palindrome. \n")
    elif choice==2:
        sub=input("Enter the Sub String:")
        x=sentence.find(sub)
        print(f"Sub String is present at {x} position. \n")
    elif choice==3:
        freq={}
        for i in sen:
            if freq in sen:
                freq[i]+=1
            else:
                freq[i]=1
        print(f"Frequency Occourance in each word is {freq}. \n")
    elif choice==4:
        exit(0)