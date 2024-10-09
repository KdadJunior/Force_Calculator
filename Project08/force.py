import copy
# import math
#
# "Magnitude: {}"
# "\nAngle: {}"
# "\nBoth objects must be of the Force class"
# "\nForce object {} already exists!"
# "\nForce object {} does not exist!"
# "\nForce #{}: {}"
# "\n{}"
#
# class Force(object):
#
#     """
#         INSERT DOCSTRING
#     """
#
#     def __init__(self, magnitude=0, angle=0):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#     def get_magnitude(self):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#     def get_angle(self):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#     def get_components(self):
#         """
#             INSERT DOCSTRING
#         """
#
#         pass
#
#
#     def __str__(self):
#         """
#             INSERT DOCSTRING
#         """
#
#         pass
#
#     def __eq__(self, other):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#     def __add__(self, other):
#         """
#             INSERT DOCSTRING
#         """
#
#         pass
#
#
# class ForceCalculator(object):
#
#     """
#         INSERT DOCSTRING
#     """
#
#     def __init__(self, forces=None):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#     def get_forces(self):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#     def add_force(self, name, magnitude, angle):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#     def remove_force(self, name):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#     def __getitem__(self, name):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#     def compute_net_force(self):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#     def __str__(self):
#         """
#             INSERT DOCSTRING
#         """
#         pass
#
#
import math

class Force:
    """
    Class to represent a force vector with a magnitude and an angle in degrees.
    """
    def __init__(self, magnitude=0, angle=0):
        """
        Initialize the Force object with a magnitude and an angle.
        Default values for both parameters are 0.
        """
        self.magnitude = float(magnitude)
        self.angle = float(angle)

    def get_magnitude(self):
        """
        Return the magnitude of the force.
        """
        return self.magnitude

    def get_angle(self):
        """
        Return the angle of the force.
        """
        return self.angle

    def get_components(self):
        """
        Calculate and return the x and y components of the force based on its magnitude and angle.
        """
        radians = math.radians(self.angle)
        x = self.magnitude * math.cos(radians)
        y = self.magnitude * math.sin(radians)
        return x, y

    def __str__(self):
        """
        Provide a string representation of the force in the format 'Magnitude: <magnitude>, Angle: <angle>'
        with values formatted to two decimal places.
        """
        return f"Magnitude: {self.magnitude:.2f}\nAngle: {self.angle:.2f}"

    def __eq__(self, other):
        """
        Compare this Force instance with another Force instance for equality based on magnitude and angle.
        Raises a RuntimeError if the other object is not an instance of Force.
        """
        if not isinstance(other, Force):
            raise RuntimeError("Both objects must be of the Force class")
        return math.isclose(self.magnitude, other.magnitude, rel_tol=1e-9) and math.isclose(self.angle, other.angle, rel_tol=1e-9)

    def __add__(self, other):
        """
        Add another Force object to this one and return a new Force object representing the resultant force.
        """
        if not isinstance(other, Force):
            raise TypeError("Both objects must be of the Force class")
        x1, y1 = self.get_components()
        x2, y2 = other.get_components()
        x_total = x1 + x2
        y_total = y1 + y2
        new_magnitude = math.sqrt(x_total**2 + y_total**2)
        new_angle = math.degrees(math.atan2(y_total, x_total)) % 360
        return Force(new_magnitude, new_angle)


class ForceCalculator:
    """
    Class to manage multiple Force objects.
    """
    def __init__(self,forces=None):
        """
        Initialize the ForceCalculator with an empty dictionary to store Force objects.
        """
        self.forces = forces
        if self.forces == None:
            self.forces = {}
        else:
            self.forces = forces

    def __getitem__(self, name):
        """
        Allows dictionary-like access to the forces by name.Returns the Force object associated
        with the given name. Raises a RuntimeError if the provided key is not of a valid type.
        """
        if not isinstance(name, str):
            raise RuntimeError("Force name must be a string.")
        if name not in self.forces:
            raise RuntimeError(f"\nForce object {name} does not exist!")
        return self.forces[name]

    def add_force(self, name, magnitude, angle):
        """
        Create a new Force object and add it to the dictionary using 'name' as the key.
        Raises a RuntimeError if the name already exists in the dictionary.
        """
        if name in self.forces:
            raise RuntimeError(f"\nForce object {name} already exists!")
        self.forces[name] = Force(magnitude, angle)

    def remove_force(self, name):
        """
        Remove the Force object associated with 'name'.
        Raises a RuntimeError if the name does not exist in the dictionary.
        """
        if name not in self.forces:
            raise RuntimeError(f"\nForce object {name} does not exist!")
        del self.forces[name]

    def get_forces(self):
        """
        Return the dictionary containing all the Force objects stored in the ForceCalculator.
        """
        return self.forces

    def compute_net_force(self):
        """
        Compute and return the net force from all the forces added to the calculator.
        Returns a default Force object if the calculator is empty.
        """
        net_force = Force()
        for force in self.forces.values():
            net_force += force
        return net_force

    def __str__(self):
        """
        Generate the string output with the name key and each part of the Force object string
        in the calculator starting on a new line. The first force starts with a newline.
        """
        if not self.forces:
            return ""
        forces_str = []
        for index, (name, force) in enumerate(self.forces.items(), start=1):
            force_description = (f"Force #{index:02d}: {name}\n" +
                                 f"Magnitude: {force.magnitude:.2f}\n" +
                                 f"Angle: {force.angle:.2f}")
            forces_str.append(force_description)
        # Join all force descriptions with newlines and prepend a newline to the first one
        return "\n" + "\n".join(forces_str)