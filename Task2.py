from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Vector3:
    x: float
    y: float
    z: float

def v_norm(v: Vector3) -> float:
    match v:
        case Vector3(x, y, z):
            return math.hypot(x, y, z)

def v_dot(u: Vector3, v: Vector3) -> float:
    match (u, v):
        case (Vector3(x1, y1, z1), Vector3(x2, y2, z2)):
            return x1 * x2 + y1 * y2 + z1 * z2

def v_cross(u: Vector3, v: Vector3) -> Vector3:
    match (u, v):
        case (Vector3(x1, y1, z1), Vector3(x2, y2, z2)):
            return Vector3(
                y1 * z2 - z1 * y2,
                z1 * x2 - x1 * z2,
                x1 * y2 - y1 * x2
            )

def v_triple(u: Vector3, v: Vector3, w: Vector3) -> float:
    match (u, v, w):
        case (Vector3(x1, y1, z1), Vector3(x2, y2, z2), Vector3(x3, y3, z3)):
            # Детермінант матриці 3x3 (мішаний добуток)
            return (
                x1 * (y2 * z3 - z2 * y3) +
                y1 * (z2 * x3 - x2 * z3) +
                z1 * (x2 * y3 - y2 * x3)
            )

u = Vector3(1.0, 2.0, 3.0)
v = Vector3(-1.0, 0.0, 2.0)
w = Vector3(2.0, 1.0, -1.0)

print("u =", u)
print("v =", v)
print("w =", w)
print("Норма ||u||       :", v_norm(u))
print("Скалярний u · v   :", v_dot(u, v))
print("Векторний u × v   :", v_cross(u, v))
print("Мішаний u·(v × w) :", v_triple(u, v, w))