from shape.shape_calc import Circle, Triangle, calculate_area, is_right_angled
from shape.shape_calc import Rectangle

circle = Circle(3.1)
triangle = Triangle(3, 4, 5)
rectangle = Rectangle(3, 4)

print(f"------------ START ------------")
print(f"")


print(f"Площадь круга: {calculate_area(circle)}")
print(f"Круг прямоугольный? {is_right_angled(circle)}")

print(f"")

print(f"Площадь треугольника: {calculate_area(triangle)}")
print(f"Треугольник прямоугольный? {is_right_angled(triangle)}")

print(f"")

print(f"Площадь прямоугольника: {calculate_area(rectangle)}")
print(f"Прямоугольник прямоугольный? {is_right_angled(rectangle)}")

print(f"")
print(f"------------ END ------------")
