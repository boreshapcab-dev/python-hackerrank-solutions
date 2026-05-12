1. "You can just as easily store a string as a variable and then print it to stdout"
    my_string=("Hello, World!")
    print(my_string)

"""2.Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird"""
    n = int(input())
    if(n%2!=0):
    print("weired")
    else if(2<=n<=5):
    prnt("Not weired")
    else if(6<=n<-20):
    print("Weired")
    else if(n>=20):
    print("Not weired")
