"""
Given an integer n, perform the following conditional actions:
If n is odd, print "Weird".
If n is even and in the inclusive range 2 to 5, print "Not Weird".
If n is even and in the inclusive range 6 to 20, print "Weird".
If n is even and greater than 20, print "Not Weird".
"""

num = int(input("Enter a number: "))

if num%2!=0:
    print("Weird")

else:

    if num in [2,3,4,5]:
        print("Not Weird")

    elif num in range(6,21):
        print("Weird")

    elif num > 20:
        print("Not Weird")
        