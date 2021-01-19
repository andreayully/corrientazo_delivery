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


def get_orientation_name(orientation):
    """
    :param orientation:
    :return: orientation name
    """
    if orientation == "N":
        return "Norte"
    elif orientation == "S":
        return "Sur"
    elif orientation == "O":
        return "Oeste"
    elif orientation == "E":
        return "Este"


def get_ort_vector(orientacion, direction):
    """
    :param orientacion: N,S,O,E
    :param direction: I, D
    :return: coordinates that will be added to the current coordinates
    """
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
    """
    :param orientacion: N,S,O,E
    :param direction: I, D
    :return: orientacion: N,S,O,E
    """
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
