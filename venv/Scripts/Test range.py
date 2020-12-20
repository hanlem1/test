# Python programme to calculate the cost of traffolite nameplates

l = float(input("Length : "))
w = float(input("Width : "))
t = float(input("Thickness : "))
q = int(input("Quantity : "))
area = l * w

cost = float(1)
totalcost = float(1)
perimeter = float(1)
perimeter = 2 * (l + w)

if int(area) in range(1, 12500):

    print(f'These {l}mm X {w}mm nameplates have have the following values')
    if area <= 200:
        cost = 1.00
    elif area > 200 and area <= 400:
        cost = 1.20
    elif area > 400 and area <= 600:
        cost = 1.30
    elif area > 600 and area <= 800:
        cost = 1.40
    elif area > 800 and area <= 1000:
        cost = 1.50
    elif area > 1000 and area <= 1500:
        cost = 1.80
    elif area > 1500 and area <= 2000:
        cost = 2.00
    elif area > 2000 and area <= 2500:
        cost = 2.40
    elif area > 2500 and area <= 3000:
        cost = 2.70
    elif area > 3000 and area <= 3500:
        cost = 2.90
    elif area > 3500 and area <= 4000:
        cost = 3.10
    elif area > 4000 and area <= 4500:
        cost = 3.30
    elif area > 4500 and area <= 5000:
        cost = 3.50
    elif area > 5000 and area <= 7500:
        cost = 3.10
    elif area > 7500 and area <= 10000:
        cost = 3.30
    elif area > 10000 and area <= 12500:
        cost = 3.50

elif float(area) in range(801, 1600):

    print("  These nameplates have an area in the range of 801mm 1600mm ")
    if area >= 801 and area <= 900:
        cost = 2.40
    elif area > 900 and area <= 1000:
        cost = 2.60
    elif area > 1000 and area <= 1100:
        cost = 2.80
    elif area > 1100 and area <= 1200:
        cost = 3.00
    elif area > 1200 and area <= 1300:
        cost = 3.20
    elif area > 1300 and area <= 1400:
        cost = 3.40
    elif area > 1400 and area <= 1500:
        cost = 3.60
    elif area > 1500 and area <= 1600:
        cost = 3.80
else:

    print("Your number wasn't in the correct range")

print(f' Area of Rectangle      : {area} mm')
print(' Perimeter of Rectangle : ', perimeter)
print(f' Unit  Cost is                              : €{cost}')
totalcost = q * cost
print(f' Total Cost is                              : €{totalcost}')