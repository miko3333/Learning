from math import *


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


class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate" + self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA == source
        else:
            if self.pinB == None:
                self.pinB == source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin == source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class XORGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


class NorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 1
        else:
            return 0


class NandGate(AndGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class NorGate(OrGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

#class HalfSummator()


g1 = NandGate("A and B")
g2 = AndGate("C and D")
g3 = NandGate("A and B")
g4 = NandGate("C and D")
c1 = Connector(g1, g2)
print(c1.getOutput())