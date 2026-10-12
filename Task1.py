from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Complex:
    re: float
    im: float

def c_add(u: Complex, v: Complex) -> Complex:
    match (u, v):
        case (Complex(a, b), Complex(c, d)):
            return Complex(a + c, b + d)

def c_sub(u: Complex, v: Complex) -> Complex:
    match (u, v):
        case (Complex(a, b), Complex(c, d)):
            return Complex(a - c, b - d)

def c_mul(u: Complex, v: Complex) -> Complex:
    match (u, v):
        case (Complex(a, b), Complex(c, d)):
            return Complex(a * c - b * d, a * d + b * c)

def c_conj(u: Complex) -> Complex:
    match u:
        case Complex(a, b):
            return Complex(a, -b)

def c_abs(u: Complex) -> float:
    match u:
        case Complex(a, b):
            return math.hypot(a, b)

z1 = Complex(3.0, 4.0)
z2 = Complex(1.0, -2.0)

print("z1 =", z1)
print("z2 =", z2)
print("Додавання (z1 + z2) :", c_add(z1, z2))
print("Віднімання (z1 - z2):", c_sub(z1, z2))
print("Множення (z1 * z2)  :", c_mul(z1, z2))
print("Спряжене conj(z1)   :", c_conj(z1))
print("Модуль |z1|         :", c_abs(z1))