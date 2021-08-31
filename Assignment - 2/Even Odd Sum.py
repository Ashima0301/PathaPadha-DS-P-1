even_sum = 0
odd_sum = 0
 
for x in range(20,31):
    if(x % 2 == 0):
        even_sum = even_sum + x
    else:
        odd_sum = odd_sum + x
 
print("The Sum of Even Numbers is : ", even_sum)
print("The Sum of Odd Numbers is : ", odd_sum)
