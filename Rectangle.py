class Rectangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_xy(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def move_up(self, y):
        self.y -= y

    def move_down(self, y):
        self.y += y

    def move_left(self, x):
        self.x -= x

    def move_right(self, x):
        self.x += x

    def position(self):
        return (self.x, self.y)

    def contains_point(self, point):
        return self.x <= point[0] and (self.x + self.width) >= point[0] \
               and self.y <= point[1] and (self.y + self.height) >= point[1]

    def contains(self, rectangle):
        top_left = (rectangle.x, rectangle.y)
        top_right = ((rectangle.x + rectangle.width), rectangle.y)
        bottom_left = (rectangle.x, (rectangle.y + rectangle.height))
        bottom_right = ((rectangle.x + rectangle.width), (rectangle.y + rectangle.height))

        return self.contains_point(top_left) or self.contains_point(top_right) \
               or self.contains_point(bottom_left) or self.contains_point(bottom_right)
