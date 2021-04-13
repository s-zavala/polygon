"""
Shape Calculator by Sofia Zavala
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        pass
    
    def set_height(self, new_height):
        pass

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (width ** 2 + height ** 2) ** 0.5
    
    def get_picture(self):
        if self.height < 50 and self.width < 50:
            return ('\*' * self.width + '\n') * self.height
        else:
            return "Too big for picture."

    def get_amount_inside(self, other_shape):
        times_into_width = self.width // other_shape.width
        times_into_height = self.height // other_shape.height
        return times_into_height * times_into_width

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, width=side, height=side)
    
    def set_height(self, new_height):
        Rectangle.set_height(new_height)
        Rectangle.set_width(new_height)
    
    def set_width(self, new_width):
        Rectangle.set_width(new_width)
        Rectangle.set_height(new_width)

    def __str__(self):
        return f"Square: side={self.width}"
