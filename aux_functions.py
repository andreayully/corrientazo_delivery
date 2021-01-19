norte = (0, 1)
oeste = (-1, 0)
sur = (0, -1)
este = (1, 0)

direction_dict = {
    'N': norte,
    'E': este,
    'S': sur,
    'O': oeste
}
vector_or = ["N", "E", "S", "O"]


def get_orientation_name(orientacion):
    if orientacion == "N":
        return "Norte"
    elif orientacion == "S":
        return "Sur"
    elif orientacion == "O":
        return "Oeste"
    elif orientacion == "E":
        return "Este"


def get_ort_vector(orientacion, direction):
    pos = vector_or.index(orientacion)
    if direction == "D":
        if pos < 3:
            pos += 1
        else:
            pos = 0
    elif direction == "I":
        if pos >= 1:
            pos -= 1
        elif pos == 0:
            pos = 3
    coord = direction_dict[vector_or[pos]]
    return coord


def get_orientation(orientacion, direction):
    pos = vector_or.index(orientacion)
    if direction == "D":
        if pos < 3:
            pos += 1
        else:
            pos = 0
    elif direction == "I":
        if pos >= 1:
            pos -= 1
        elif pos == 0:
            pos = 3
    orientacion = vector_or[pos]
    return orientacion
