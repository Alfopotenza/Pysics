from matplotlib import pyplot as plt
from PyMath import *


class Vector:
    def __init__(self, module, direction):
        self.module = module
        self.direction = direction

    def __str__(self):
        return str(f"module: {self.module}, direction: {self.direction}")

    def show(self, ax: plt.Axes, origin: [float, float], color: str) -> object:
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

    def __neg__(self):
        if self.direction + 180 >= 360:
            return Vector(self.module, self.direction - 180)
        elif self.direction - 180 < 0:
            return Vector(self.module, self.direction + 180)
        else:
            return Vector(self.module, self.direction + 180)

    def get_comps(self, env, **comps):
        steepness = env.steepness
        if comps.get("x") is None and comps.get("y") is None:
            comp_x = Vector(self.module * sin(steepness), self.direction + 90 - steepness)
            comp_y = Vector(self.module * cos(steepness), self.direction - steepness)
            return {"x": comp_x, "y": comp_y}
        else:
            mod = comps.get("x").module / sin(steepness)
            _dir = 270
            return Vector(mod, _dir)


class Object:
    _vars = {}
    forces = []

    def __init__(self, environment, **_vars):
        #here all the variables that can exist will be added
        self.hooke_force = None
        self.weight = None
        self.acceleration = None

        self._vars = _vars
        self.env = environment

        self.mass = _vars.get("mass")

    def show_obj(self, _ax, origin, color, size):
        return _ax.add_patch(plt.Circle(origin, size, color=color))

    def show_forces(self, _ax, origin, color):
        for force in self.forces:
            print(force)
            force.show(_ax, origin, color)

    def add_force(self, **variables):
        force = Vector(module=variables.get("force"), direction=variables.get("direction"))
        self.forces.append(force)

    def hooke_law(self, **variables):
        force = variables.get("force")
        hooke_constant = variables.get("constant")
        spring_length = variables.get("length")
        spring_dir = variables.get("spring_dir")
        if force is None:
            return Vector(hooke_constant * spring_length, spring_dir)
        if hooke_constant is None:
            return force.module / spring_length
        if spring_length is None:
            return force.module / hooke_constant

    def newton_first_law(self, **variables):
        self.weight: Vector = variables.get("weight")
        self.acceleration = self.env.gravity
        if self.weight is None or self.weight.module == 0:
            return Vector(self.mass * self.acceleration, 270)
        if self.mass is None:
            return self.weight.module / self.acceleration
        if self.acceleration is None:
            return self.weight.module / self.mass

    def friction_law(self, env, **variables):
        steepness = env.steepness
        force: Vector = variables.get("force")
        pressing = variables.get("pressing")
        fric_constant = variables.get("constant")
        if force is None or force.module == 0:
            return Vector(fric_constant * pressing.module, 180 - steepness)
        elif pressing.module is None:
            return force.module / fric_constant
        elif fric_constant is None:
            print("CHECK")
            return force.module / pressing.module


class Environment:
    def __init__(self, **_vars):
        self.gravity = _vars.get("gravity")
        self.steepness = _vars.get("steepness")
