name = input("Enter name: ")
ph = float(input("Enter grade in Physics: "))
al = float(input("Enter grade in Algebra: "))
pr = float(input("Enter grade in Programming: "))
ave = float( ph + al + pr ) / 3

out = print(f'{name} average grade is {ave}')

if ave > 100:
    print("Invalid grade")
    exit()
if ave >= 95:
    print("President lister")
    exit()
if ave >= 89:
    print("Dean lister")
    exit()
if ave >= 83:
    print("Average Student")
    exit()
if ave >= 78:
    print("Fair")
    exit()
else:
    print("Failure")
