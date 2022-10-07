pname = input("Enter product: ")
price = float(input("Enter price: "))
dis = float()
net = float()

if price > 100000:
    dis = price * 0.20
    net = float(price - dis)
    print(f'Price of {pname} is {price}')
    print(f'Discount is {dis}')
    print(f'Net Price is {net}')
    exit()

if price > 50000:
    dis = price * 0.15
    net = float(price - dis)
    print(f'Price of {pname} is {price}')
    print(f'Discount is {dis}')
    print(f'Net Price is {net}')
    exit()

if price > 20000:
    dis = price * 0.1
    net = float(price - dis)
    print(f'Price of {pname} is {price}')
    print(f'Discount is {dis}')
    print(f'Net Price is {net}')
    exit()

if price > 10000:
    dis = price * 0.05
    net = float(price - dis)
    print(f'Price of {pname} is {price}')
    print(f'Discount is {dis}')
    print(f'Net Price is {net}')
    exit()


else:
    dis = 0
    net = float(price)
    print(f'Price of {pname} is {price}')
    print(f'Discount is {dis}')
    print(f'Net Price is {net}')

