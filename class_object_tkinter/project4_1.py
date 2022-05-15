# Single Inheritace
class rect:
    def rect_area(a, height, width):
        area = height* width
        print("The area of the rectangle is ", area)
class square(rect):
    def square_area(a, side):
        area = side * side
        print("The area of the square is ", area)
b1 = square()
b1.rect_area(3,5)
b1.square_area(5)