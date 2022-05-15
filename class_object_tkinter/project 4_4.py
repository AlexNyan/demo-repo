# Hierarchical Inheritance
class rect:
    def rect_area(a, height, width):
        area = height* width
        print("The area of the rectangle is ", area)
class square(rect):
    def square_area(a, side):
        area = side * side
        print("The area of the square is ", area)
class triangle(rect):
    def tri_area(a, breadth, width):
        area = 0.5 * breadth * width
        print("The area of the triangle is " ,area)
b1 = triangle()
b1.rect_area(3,7)
b1.tri_area(5,6)
