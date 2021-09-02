str=str(input("Enter a string: "))  
if len(str) < 2:
       print("empty string")
else:
       str1=str[0:2] + str[-2:]
       print("new string: ", str1)

