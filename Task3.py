from __future__ import annotations
from dataclasses import dataclass
import math

# ADT для 2D-вектора (для лінійних перетворень)
@dataclass(frozen=True)
class Vector2:
    x: float
    y: float

# ADT для матриці 2x2
@dataclass(frozen=True)
class Matrix2:
    a: float
    b: float
    c: float
    d: float

def m_det(m: Matrix2) -> float:
    match m:
        case Matrix2(a, b, c, d):
            return a * d - b * c

def m_inv(m: Matrix2) -> Matrix2:
    match m:
        case Matrix2(a, b, c, d):
            det = a * d - b * c
            if math.isclose(det, 0.0, abs_tol=1e-12):
                raise ValueError("Матриця є виродженою (det = 0)")
            # Пряме ділення та округлення усувають похибку float
            return Matrix2(
                round(d / det, 10),
                round(-b / det, 10),
                round(-c / det, 10),
                round(a / det, 10)
            )

def m_mul(m1: Matrix2, m2: Matrix2) -> Matrix2:
    match (m1, m2):
        case (Matrix2(a1, b1, c1, d1), Matrix2(a2, b2, c2, d2)):
            return Matrix2(
                round(a1 * a2 + b1 * c2, 10),
                round(a1 * b2 + b1 * d2, 10),
                round(c1 * a2 + d1 * c2, 10) + 0.0,
                round(c1 * b2 + d1 * d2, 10)
            )

def m_transform(m: Matrix2, v: Vector2) -> Vector2:
    """Лінійне перетворення: множення матриці 2x2 на вектор 2D"""
    match (m, v):
        case (Matrix2(a, b, c, d), Vector2(x, y)):
            return Vector2(
                round(a * x + b * y, 10),
                round(c * x + d * y, 10)
            )

m1 = Matrix2(4.0, 7.0, 2.0, 6.0)
m2 = Matrix2(1.0, 2.0, 3.0, 4.0)
v = Vector2(1.0, 2.0)

print("m1 =", m1)
print("m2 =", m2)
print("v  =", v)
print("det(m1)              =", m_det(m1))

inv_m1 = m_inv(m1)
print("inv(m1)              =", inv_m1)
print("Перевірка m1 @ inv1  =", m_mul(m1, inv_m1))
print("Добуток m1 @ m2      =", m_mul(m1, m2))
print("Лінійне перетв. m1·v =", m_transform(m1, v))