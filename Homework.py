from math import *


class Fraction:
    def __init__(self, top, bottom):
        if isinstance(top, int) and isinstance(bottom, int):
            self.numerator = top
            self.denominator = bottom
        elif top < 0 and bottom < 0:
            self.numerator = -top
            self.denominator = -bottom
        elif top > 0 and bottom < 0:
            self.numerator = -top
            self.denominator = bottom
        else:
            raise RuntimeError("Must be int")


    def show(self):
        print(self.numerator, "/", self.denominator)

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def __add__(self, other_fraction):
        new_numerator = self.numerator*other_fraction.denominator + self.denominator*other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator//common, new_denominator//common)

    def __radd__(self, other_fraction):
        new_numerator = self.denominator*other_fraction.numerator + self.numerator*other_fraction.denominator
        new_denominator = other_fraction.denominator * self.denominator
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator//common, new_denominator//common)
    """
    def __iadd__(self, other_fraction): #hz chto ne rabotaet
        new_numerator = self.denominator * other_fraction.numerator + self.numerator * other_fraction.denominator
        new_denominator = other_fraction.denominator * self.denominator
        self.numerator += new_numerator
        self.denominator += 
        common = gcd(self.numerator, self.denominator)
        return Fraction(self.numerator//common, self.denominator//common)
    """

    def __eq__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator
        return first_num == second_num

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator//common, new_denominator//common)

    def __sub__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator//common, new_denominator//common)

    def __lt__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator
        return first_num < second_num

    def __gt__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator
        return first_num > second_num

    def __ge__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator
        return first_num >= second_num

    def __le__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator
        return first_num <= second_num

    def __ne__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator
        return first_num != second_num

    def getNum(self):
        return self.numerator

    def getDen(self):
        return self.denominator

    def __repr__(self):
        return "Fraction(%r, %r)" % (self.numerator, self.denominator)



f1 = Fraction(1, 4)
f2 = Fraction(1, 4)
print(f1 > f2)
print(f1 >= f2)
print(f1 <= f2)
print(f1 < f2)
print(f1 != f2)
print(repr(f1))
