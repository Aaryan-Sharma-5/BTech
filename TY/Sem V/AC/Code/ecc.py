import time
from typing import Optional, Tuple

class ECCPoint:
    def __init__(self, x: Optional[int], y: Optional[int], a: int, b: int, p: int):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.p = p
        
        if not self.is_infinity() and not self.is_on_curve():
            raise ValueError(f"Point ({x}, {y}) is not on the curve")
    
    def is_infinity(self) -> bool:
        return self.x is None and self.y is None
    
    def is_on_curve(self) -> bool:
        if self.is_infinity():
            return True
        
        left_side = (self.y * self.y) % self.p
        right_side = (self.x * self.x * self.x + self.a * self.x + self.b) % self.p
        return left_side == right_side
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, ECCPoint):
            return False
        return (self.x == other.x and self.y == other.y and 
                self.a == other.a and self.b == other.b and self.p == other.p)
    
    def __str__(self) -> str:
        if self.is_infinity():
            return "O"
        return f"({self.x}, {self.y})"


def mod_inverse(a: int, m: int) -> int:
    if a < 0:
        a = (a % m + m) % m
    
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse of {a} mod {m} does not exist")
    return (x % m + m) % m


class EllipticCurve:
    def __init__(self, a: int, b: int, p: int):
        self.a = a
        self.b = b
        self.p = p
        
        discriminant = (4 * a * a * a + 27 * b * b) % p
        if discriminant == 0:
            raise ValueError("Curve is singular")
    
    def point_at_infinity(self) -> ECCPoint:
        return ECCPoint(None, None, self.a, self.b, self.p)
    
    def create_point(self, x: int, y: int) -> ECCPoint:
        return ECCPoint(x, y, self.a, self.b, self.p)
    
    def point_addition(self, P: ECCPoint, Q: ECCPoint) -> ECCPoint:
        if P.is_infinity():
            return Q
        if Q.is_infinity():
            return P
        if P == Q:
            return self.point_doubling(P)
        if P.x == Q.x and (P.y + Q.y) % self.p == 0:
            return self.point_at_infinity()
        
        denominator = (Q.x - P.x) % self.p
        numerator = (Q.y - P.y) % self.p
        lambda_slope = (numerator * mod_inverse(denominator, self.p)) % self.p
        
        x3 = (lambda_slope * lambda_slope - P.x - Q.x) % self.p
        y3 = (lambda_slope * (P.x - x3) - P.y) % self.p
        
        return self.create_point(x3, y3)
    
    def point_doubling(self, P: ECCPoint) -> ECCPoint:
        if P.is_infinity() or P.y == 0:
            return self.point_at_infinity()
        
        numerator = (3 * P.x * P.x + self.a) % self.p
        denominator = (2 * P.y) % self.p
        lambda_slope = (numerator * mod_inverse(denominator, self.p)) % self.p
        
        x3 = (lambda_slope * lambda_slope - 2 * P.x) % self.p
        y3 = (lambda_slope * (P.x - x3) - P.y) % self.p
        
        return self.create_point(x3, y3)
    
    def scalar_multiplication(self, k: int, P: ECCPoint) -> ECCPoint:
        if k == 0:
            return self.point_at_infinity()
        if k < 0:
            return self.scalar_multiplication(-k, self.point_negation(P))
        
        binary_k = bin(k)[2:]
        result = self.point_at_infinity()
        addend = P
        
        for bit in reversed(binary_k):
            if bit == '1':
                result = self.point_addition(result, addend)
            addend = self.point_doubling(addend)
        
        return result
    
    def point_negation(self, P: ECCPoint) -> ECCPoint:
        if P.is_infinity():
            return self.point_at_infinity()
        return self.create_point(P.x, (-P.y) % self.p)


class ECDLPSolver:
    def __init__(self, curve: EllipticCurve):
        self.curve = curve
    
    def brute_force_ecdlp(self, G: ECCPoint, Q: ECCPoint, max_attempts: int = 10000) -> Tuple[Optional[int], int, float]:
        start_time = time.time()
        current_point = self.curve.point_at_infinity()
        
        for d in range(max_attempts + 1):
            if current_point == Q:
                elapsed_time = time.time() - start_time
                return d, d + 1, elapsed_time
            current_point = self.curve.point_addition(current_point, G)
        
        elapsed_time = time.time() - start_time
        return None, max_attempts, elapsed_time
    
    def find_generator_point(self, curve: EllipticCurve) -> Optional[ECCPoint]:
        for x in range(curve.p):
            y_squared = (x * x * x + curve.a * x + curve.b) % curve.p
            y = self.sqrt_mod_p(y_squared, curve.p)
            if y is not None:
                return curve.create_point(x, y)
        return None
    
    def sqrt_mod_p(self, a: int, p: int) -> Optional[int]:
        if a == 0:
            return 0
        if p < 1000:
            for y in range(p):
                if (y * y) % p == a:
                    return y
        return None


def test_basic_operations():
    print("ECC Operations Test")
    print("===================")
    
    curve = EllipticCurve(a=2, b=2, p=17)
    P = curve.create_point(5, 1)
    Q = curve.create_point(6, 3)
    
    print(f"Curve: y² = x³ + 2x + 2 (mod 17)")
    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"P + Q = {curve.point_addition(P, Q)}")
    print(f"2P = {curve.point_doubling(P)}")
    print(f"3P = {curve.scalar_multiplication(3, P)}")


def test_ecdlp():
    print("\nECDLP Brute Force Test")
    print("======================")
    
    curve = EllipticCurve(a=1, b=1, p=23)
    solver = ECDLPSolver(curve)
    generator = solver.find_generator_point(curve)
    
    if generator:
        secret_d = 7
        target_Q = curve.scalar_multiplication(secret_d, generator)
        print(f"Generator G: {generator}")
        print(f"Secret d = {secret_d}")
        print(f"Target Q = {target_Q}")
        
        found_d, attempts, time_taken = solver.brute_force_ecdlp(generator, target_Q, 100)
        
        if found_d == secret_d:
            print(f"Success! Found d = {found_d} in {attempts} attempts ({time_taken:.6f}s)")
        else:
            print(f"Failed to find d within {attempts} attempts")

if __name__ == "__main__":
    test_basic_operations()
    test_ecdlp()