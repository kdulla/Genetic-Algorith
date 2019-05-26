from math import cos, sin, radians, atan2

class Car:
    def __init__(self, x, y, width = 35, length = 20, direction = 0, \
                 speed = 0, max_speed = 6, accel_force = 0.3, turn_speed = 5):

        self.x = x
        self.y = y
        self.width = width
        self.length = length

        self.dx = speed * cos(radians(direction))
        self.dy = speed * sin(radians(direction))
        self.direction = direction

        self.max_speed = max_speed
        self.accel_force = accel_force
        self.turn_speed = turn_speed

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def accel(self):
        self.dx += self.accel_force * cos(radians(self.direction))
        self.dy += self.accel_force * sin(radians(self.direction))
        if (self.dx ** 2 + self.dy ** 2) ** 0.5 > self.max_speed:
            direction = atan2(self.dy, self.dx)
            self.dx = self.max_speed * cos(direction)
            self.dy = self.max_speed * sin(direction)

    def deccel(self, ds):
        self.dx -= accel * cos(direction)
        self.dy -= accel * sin(direction)

    def turn_left(self):
        self.direction -= self.turn_speed

    def turn_right(self):
        self.direction += self.turn_speed

    def get_points(self):
        dxx = self.width * cos(radians(self.direction)) / 2
        dxy = self.width * sin(radians(self.direction)) / 2

        dyx = self.length * cos(radians(self.direction + 90)) / 2
        dyy = self.length * sin(radians(self.direction + 90)) / 2

        bottom_left = (self.x - dxx + dyx, self.y - dxy + dyy)
        top_right = (self.x + dxx - dyx, self.y + dxy - dyy)
        top_left = (self.x - dxx - dyx, self.y - dxy - dyy)
        bottom_right = (self.x + dxx + dyx, self.y + dxy + dyy)

        return (top_left, bottom_left, bottom_right, top_right)

    def draw(self, cv):
        return cv.create_polygon(*self.get_points(), fill = "black")



def are_counter_clockwise(a, B, c):
    return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])

