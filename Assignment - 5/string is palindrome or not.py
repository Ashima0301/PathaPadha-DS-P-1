def PalindromeOrNot(st):
    if(len(st)==0):
        print("empty string")
    else:
        st1=st[::-1]
        if(st1==st):
            print("The String is Palindrome")
        else:
            print("The String is not Palindrome")
st=str(input("Enter the string : "))
PalindromeOrNot(st)
