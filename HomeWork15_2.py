class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        denom = self.b * other.b
        num = self.a * other.b + other.a * self.b
        return Fraction(num, denom)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        denom = self.b * other.b
        num = self.a * other.b - other.a * self.b
        return Fraction(num, denom)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.a * other.a, self.b * other.b)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
#print(f_c)
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
#print(f_d)
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
#print(f_e)
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c # True
assert f_d > f_e # True
assert f_a != f_b # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2 # True

print('OK')