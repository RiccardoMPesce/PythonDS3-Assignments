def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        if type(top) is not int or type(bottom) is not int:
            raise Exception("Values must be integers")

        cmmn = gcd(top, bottom)
        
        self.num = top if bottom > 0 else - top
        self.den = abs(bottom)

        self.num //= cmmn 
        self.den //= cmmn

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        
        return Fraction(new_num, new_den)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        
        return Fraction(new_num, new_den)
    
    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        
        cmmn = gcd(new_num, new_den)

        return Fraction(new_num // cmmn, new_den // cmmn)
    
    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        
        cmmn = gcd(new_num, new_den)

        return Fraction(new_num // cmmn, new_den // cmmn)

    def __radd__(self, other_fraction):
        return self.__add__(other_fraction)
    
    def __iadd__(self, other_fraction):
        new_fraction = self.__add__(other_fraction)
        self.num = new_fraction.num
        self.den = new_fraction.den

        return new_fraction

    def __repr__(self):
        return f"Fraction({self.num} / {self.den})"

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den