import math
class Operation:

    @staticmethod
    def add(a: float, b: float) -> float:
        return a+b

    @staticmethod
    def subtract(a:float,b:float) -> float:
        return a-b

    @staticmethod
    def multiply(a:float,b:float) -> float:
        return a*b

    @staticmethod
    def divide(a:float,b:float) -> float:
        if b==0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a/b

    @staticmethod
    def power (base: float, exponent:float) ->float:
        return base ** exponent

    @staticmethod
    def sqrt(value: float) -> float:
        if value <0:
            raise ValueError("Cannot take square root of a negative numbers")
        return math.sqrt(value)

    @staticmethod
    def factorial(n:int) -> int:
        if n<0:
            raise ValueError("Factorial is not defined for negative numbers")

        if not float(n).is_integer():
            raise ValueError("Factorial requires an integer")
        return math.factorial(int(n))

    @staticmethod
    def sin(angle:float) ->float:
        return math.sin(angle)

    @staticmethod
    def cos (angle:float) -> float:
        return math.cos(angle)

    @staticmethod
    def tan(angle:float) -> float:
        return math.tan(angle)

    @staticmethod
    def log(value:float , base:float=10):
        if value <=0:
            raise ValueError("Logarithm requires a positive number")
        if base <= 0 or base==1:
            raise ValueError("Log base must be positive and not equal to 1")
        return math.log(value , base)

    @staticmethod
    def percent(value:float , rate : float) -> float:
        return value * rate /100

    @staticmethod
    def mod(a:float , b: float) -> float:
        if b==0:
            raise ZeroDivisionError("Cannot module by zero")
        return a%b

    @staticmethod
    def floor_division(a:float , b:float) -> float:
        if b==0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a//b