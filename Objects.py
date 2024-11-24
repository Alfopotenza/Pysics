from matplotlib import pyplot as plt
from PyMath import *


class Vector:
    def __init__(self, module, direction):
        self.module = module
        self.direction = direction

    def __str__(self):
        return str(f"module: {self.module}, direction: {self.direction}")

    def show(self, ax: plt.Axes, origin: [float, float], color: str):
        ax.quiver(origin[0], origin[1], self.module * cos(self.direction), self.module * sin(self.direction),
                  scale_units='xy', scale=1, angles='xy', color=color)

    def __add__(self, other):
        if self == other:
            if self.direction == other.direction:
                return Vector(self.module + other.module, self.direction)
            else:
                new_module = self.module - other.module
                if new_module < 0:
                    self.direction = self.direction + 180 if self.direction < 180 else self.direction - 180
                return Vector(new_module, self.direction)
        else:
            a_angle = self.direction
            b_angle = other.direction
            a_x = self.module * cos(a_angle)
            a_y = self.module * sin(a_angle)
            b_x = other.module * cos(b_angle)
            b_y = other.module * sin(b_angle)
            x = a_x + b_x
            y = a_y + b_y
            mod = pythagorean_theorem(x, y)
            print(f"y: {y}, x: {x}, _dir: {atan2(x, y)}")
            _dir = rad2deg(atan2(y, x))
            return Vector(module=mod,
                          direction=_dir)

    def __eq__(self, other):
        if self.direction == other.direction:
            return True
        elif self.direction >= 180:
            return other.direction == (self.direction - 180)
        elif self.direction < 180:
            return self.direction == (other.direction + 180)


a = Vector(10, 0)
b = Vector(10, 90)
c = Vector(20, 270)

print(a + b + c)
_origin = [0, 0]
fig, axes = plt.subplots()
a.show(axes, _origin, "y")
b.show(axes, _origin, "r")
c.show(axes, _origin, "k")
(a + b).show(axes, _origin, "g")
(a + b + c).show(axes, _origin, "b")
axes.set_xlim([-40, 40])
axes.set_ylim([-40, 40])
plt.grid()
plt.show()
