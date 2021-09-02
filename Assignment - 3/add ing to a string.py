str1=str(input("Enter a string: "))
length = len(str1)
if length < 3:
      print(str1)
else:
    if str1[-3:] == 'ing':
        print(str1[:length-3]+'ly')
    else:
        print(str1+'ing')
         

