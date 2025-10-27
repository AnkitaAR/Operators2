a=10  #true
b=15 #true
c=0 #false

if a and b and c:
    print("All are boolean values")
else:
    print("All are not boolean values")

a=10
b=-10
c=0
print("For a and b")
if a>0 or b>0:
    print("Either of the number is greater than 0")
else:
    print("None of them are greater than 0")

print("For c and b")
if b>0 or c>0:
    print("Either of the number is greater than 0")
else:
    print("None of them are greater than 0")
