import math
from abc import ABC, abstractmethod
from typing import Union, Tuple

class Shape(ABC):
    """Базовый класс для любых] фигур."""
    
    @abstractmethod
    def area(self) -> float:
        """Возвращает площадь фигуры."""
        pass
    
    @abstractmethod
    def is_right_angled(self) -> bool:
        """Возвращает True, если фигура прямоугольная."""
        pass

class Circle(Shape):  
    def __init__(self, radius: float):
        """
        Радиус круга (должен быть положительным).
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def is_right_angled(self) -> bool:
        """Круг не прямоугольный, всегда вернуть False."""
        return False

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        """
        Args:
            a,b,c : Длина первой, второй и третьей стороны
        Raises:
            ValueError: Если стороны не могут образовать треугольник.
        """
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны должны быть положительными числами")
        
        sides_sorted = sorted(sides)
        if sides_sorted[0] + sides_sorted[1] <= sides_sorted[2]:
            raise ValueError("Сумма двух меньших сторон должна быть больше третьей стороны")
        
        self.a = a
        self.b = b
        self.c = c
    
    def area(self) -> float:
        """Вычисляет площадь треугольника по формуле Герона."""
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def is_right_angled(self, tolerance: float = 1e-6) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным.
        Args:
            tolerance: Допустимая погрешность при сравнении.
        Returns:
            True, если треугольник прямоугольный, иначе False.
        """
        sides = sorted([self.a, self.b, self.c])
        # Проверяем теорему Пифагора с допуском
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tolerance

def calculate_area(shape: Union[Circle, Triangle, Shape]) -> float:
    """
    Вычисляет площадь фигуры любого типа.
    Returns:
        Площадь фигуры.
    """
    return shape.area()

def is_right_angled(shape: Union[Circle, Triangle, Shape]) -> bool:
    """
    Проверяет, является ли фигура прямоугольной (если применимо).. 
    Returns:
        True, если фигура прямоугольная, иначе False.
    """
    return shape.is_right_angled()


class Rectangle(Shape):
    """Класс для прямоугольника наследуется от Shape."""
    
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def is_right_angled(self) -> bool:
        return True  # Прямоугольник всегда прямоугольный