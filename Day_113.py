# ========================== Question =========================
#
# Create a class Rectangle that stores the length and breadth of
# a rectangle and has two methods: area() and perimeter().
#
# You are given N rectangles. Your task is to print the area and
# perimeter of each rectangle.
#
# Example:
#
# Input:
# 3
# 3 4
# 5 2
# 6 6
#
# Area of 3 x 4 = 12, Perimeter = 2 * (3 + 4) = 14
#
# Output:
# Area: 12 Perimeter: 14
# Area: 10 Perimeter: 14
# Area: 36 Perimeter: 24
#
# Important Point:
#
# __init__ stores the values in self, and every method receives
# self so it can use those stored values.
#
# ============================================================

# ======================= Solution ==========================
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


n = int(input())

for _ in range(n):
    length, breadth = map(int, input().split())
    rect = Rectangle(length, breadth)
    print(f"Area: {rect.area()} Perimeter: {rect.perimeter()}")
