#Python programme to calculate the cost of traffolite nameplates

l=float(input("Length : "))
w=float(input("Width : "))
t=float(input("Thickness : "))
q=int(input("Quantity : "))
area=l*w
perimeter=2*(l+w)
#cost=float(0)
max=float(180000)

if int(area) in range(1, 800):

    print("These nameplates have an area in the range of 1mm 800mm ")
    if area <= 200:
        cost = 1.20
    elif area > 200 and area <= 300:
        cost = 1.40
    elif area > 300 and area <= 400:
        cost = 1.60
    elif area > 400 and area <= 500:
        cost = 1.80
    elif area > 500 and area <= 600:
        cost = 2.00
    elif area > 600 and area <= 700:
        cost = 2.20
    elif area > 700 and area <= 800:
        cost = 2.40
elif float(area) in range(801, 180000):

    print("These nameplates have an area in the range of 801mm 1600mm ")
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
    elif area > max:
        print(f'The area calculated is larger than a sign we make {max}')





print("Area of Rectangle : ", area)
print('Perimeter of Rectangle : ', perimeter)
print ("Cost per item is ", cost)
totalcost = q*cost
print ("Total cost is ", totalcost )