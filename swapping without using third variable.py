x = int(input("Enter the 1st number : "))
y = int(input("Enter the 2nd number : ")) 
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# Swap code
x = x + y
y = x - y 
x = x - y 
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
