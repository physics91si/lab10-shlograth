#!/usr/bin/python
import sys

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    x1, x2 = find_roots(a, b, c)
    print ("This is x1: %f" %x1)
    print ("This is x2: %f" %x2)


def find_roots(a,b,c):
    try:
        mid = (b**2) - (4*a*c)
        assert [mid > 0], "We don't delve into the realm of the imaginary in these parts" 
        sqrt_mid = mid**(1./2)
        x1 = (-b + sqrt_mid)/(2*a)
        x2 = (-b - sqrt_mid)/(2*a)
        return x1, x2
    except ZeroDivisionError:
        print("You know what you did")
    except TypeError:
        print("You didn't input a number")



if __name__=="__main__":
        main()
