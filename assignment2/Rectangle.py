class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def compare_area(self, other_rectangle):
        area1 = self.calculate_area()
        area2 = other_rectangle.calculate_area()
        if area1 == area2:
            return "The rectangles have the same area."
        elif area1 > area2:
            return "The first rectangle has a larger area."
        else:
            return "The second rectangle has a larger area."

# Create two Rectangle objects
rectangle1 = Rectangle(5, 4)
rectangle2 = Rectangle(3, 6)

# Calculate and print the area and perimeter of each rectangle
print("Rectangle 1:")
print("Area:", rectangle1.calculate_area())
print("Perimeter:", rectangle1.calculate_perimeter())

print("\nRectangle 2:")
print("Area:", rectangle2.calculate_area())
print("Perimeter:", rectangle2.calculate_perimeter())

# Compare the two rectangles based on their areas
comparison_result = rectangle1.compare_area(rectangle2)
print("\nComparison Result:", comparison_result)
