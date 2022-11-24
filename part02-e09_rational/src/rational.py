#!/usr/bin/env python3

class Rational(object):
    def __init__(self, param1, param2):
        self.numerator = param1
        self.denominator = param2

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __mul__(self, other):  
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Rational(numerator, denominator)

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __eq__(self, other):
        return (self.numerator * other.denominator - other.numerator * self.denominator) / (self.denominator * other.denominator) == 0

    def __gt__(self, other):
        return (self.numerator * other.denominator - other.numerator * self.denominator) / (self.denominator * other.denominator) > 0

    def __lt__(self, other):
        return (self.numerator * other.denominator - other.numerator * self.denominator) / (self.denominator * other.denominator) < 0

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
