from ops.add import add
from ops.avg import avg
from ops.divide import divide
from ops.mod import mod
from ops.multiply import multiply
from ops.power import power
from ops.subtract import subtract

operations = {
    "+": add,
    "%": mod,
    "*": multiply,
    "-": subtract,
    "/": divide,
    "**": power,
    "avg": avg,
}
