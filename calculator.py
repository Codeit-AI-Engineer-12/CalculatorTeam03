from ops.add import add
from ops.mod import mod
from ops.multiply import multiply
from ops.subtract import subtract
from ops.divide import divide
from ops.power import power

operations = {
    "+": add,
    "%": mod,
    "*": multiply,
    "-": subtract,
    "/": divide,
    "**": power,
}
