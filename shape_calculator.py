"""
Shape Calculator by Sofia Zavala
04/13/2021
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height < 50 and self.width < 50:
            pic_width = '*' * self.width + '\n'
            return pic_width * self.height
        else:
            return "Too big for picture."

    def get_amount_inside(self, other_shape):
        amt = self.get_area() // other_shape.get_area()
        return amt

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, width=side, height=side)

    def set_side(self, new_side):
        Rectangle.set_width(self, new_side)
        Rectangle.set_height(self, new_side)

    def __str__(self):
        return f"Square(side={self.width})"


if __name__ == '__main__':
    t1 = Rectangle(15, 20)
    t1.set_width(16)
    t1.set_height(21)
    a = t1.get_area()
    b = t1.get_perimeter()
    c = t1.get_diagonal()
    d = t1.get_picture()
    t2 = Rectangle(3, 4)
    e = t1.get_amount_inside(t2)
    print(t1)
    print(t2)
    t3 = Square(3)
    t3.set_height(4)
    t3.set_width(5)
    print(t3)
    f = t1.get_amount_inside(t3)
    g = t2.get_amount_inside(t3)
    print('spam')
