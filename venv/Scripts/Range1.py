#r = range (12500, 140000, 2500)
#type( r )

#r = list( r )
#type( r )

#print(r)

print("Range() Test")
for i in range(12500, 140000, 2500):
    if i == 60:
        print('Break Point')
        break
    print(i)
