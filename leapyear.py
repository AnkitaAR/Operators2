year=int(input("Enter the year to check whether it is a leap year:"))
if year%400==0 and year%100==0:
    print("It is a leap year")
elif year%4==0 and year%100!=0:
    print("It is a leap year")
else:
    print("Not a leap year")
