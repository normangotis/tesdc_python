s = input("Enter String: ")
x = int(input("Enter number of times: "))
p = 0

if x <= 0:
    print("Invalid input, program ends")
else:
    while p < x:
        print(s)
        p += 1

