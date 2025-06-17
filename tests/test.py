import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import unittest
import math
from shape.shape_calc import Circle, Triangle, calculate_area, is_right_angled

class TestShapes(unittest.TestCase):
    
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)
        
    def test_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)
    
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)
        
    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # Не может быть треугольника
        
    def test_right_angled_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())
        
        triangle2 = Triangle(3, 4, 6)
        self.assertFalse(triangle2.is_right_angled())
    
    def test_circle_not_right_angled(self):
        circle = Circle(5)
        self.assertFalse(circle.is_right_angled())
    
    def test_calculate_area_polymorphism(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [calculate_area(shape) for shape in shapes]
        self.assertAlmostEqual(areas[0], math.pi * 4)
        self.assertAlmostEqual(areas[1], 6.0)
    
    def test_is_right_angled_polymorphism(self):
        shapes = [Circle(2), Triangle(3, 4, 5), Triangle(2, 3, 4)]
        results = [is_right_angled(shape) for shape in shapes]
        self.assertEqual(results, [False, True, False])

if __name__ == '__main__':
    unittest.main()