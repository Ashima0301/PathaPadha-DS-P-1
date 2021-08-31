num = int(input("Enter a number: "))
for x in range(2, 8):
    if (num % x) == 0:
        print(num, "is not a prime number")
        break
    else:
        print(num, "is a prime number")
        break
