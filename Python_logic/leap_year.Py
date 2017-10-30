def leapyr(n):
    if n%400==0:
        print("Leap Year")
    elif n%100==0:
        print("Not A Leap Year")
    elif n%4==0:
        print("Leap Year")
    else:
        print("Not a Leap Year")

leapyr(2000)
