#SEBASTIAN JOAQUIN N. YDIA
#8 CAMIA
# 08 27 26
#ACTIVITY 3


import math
#INPUT
print("ENTER THE LENGTH OF SHORTER SIDES OF THE RIGHT TRIANGLE TO GET THE HYPOTENUSE.")
a = float(input("enter the length of the short side 1 of the triangle: "))
b = float(input("enter the length of the short side 2 of the triangle: "))

#PROCESS
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

#OUTPUT
print(f'THE HYPOTENUSE OF A RIGHT TRIANGLE WITH SIDE LENGTHS {a} AND {b} IS {c}')