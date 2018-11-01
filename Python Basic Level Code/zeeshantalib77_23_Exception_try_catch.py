#----------------------------------- try except
# when you input chracter instead of number

try:
     no=int(input("Enter a no"))
     print(no)
except:
     print("Invalid No")

#------------- -------------------- ank other try except
try:
    10/0
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invlaid number")
