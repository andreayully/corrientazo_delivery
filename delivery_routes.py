from aux_functions import *
import os


class Punto:
    """
    Class that stores the properties of points
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def sum_x(self, orientation):
        return self.x + orientation[0]

    def sum_y(self, orientation):
        return self.y + orientation[1]


def read_order_file():
    """
    Read order_file from input console
    :return: final coordinates
    """
    try:
        file_path = input("INGRESE EL ARCHIVO DE RUTAS: ")
        file = open(file_path, "r")
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            raise Exception
    except FileNotFoundError:
        print("the indicated file does not exist")
        exit()
    except Exception:
        print("File empty")
        exit()
    drone_id = file_path.split(".")[0].replace("in", "")
    current_position = Punto(0, 0)
    current_X = 0
    current_y = 0
    orientation = "N"
    coord = get_ort_vector(orientation, "A")
    out_list = []
    for order in file:
        for ord in order:
            if "A" in ord:
                current_X += current_position.sum_x(coord)
                current_y += current_position.sum_y(coord)
            elif "D" in ord:
                coord = get_ort_vector(orientation, "D")
                orientation = get_orientation(orientation, "D")
            elif "I" in ord:
                coord = get_ort_vector(orientation, "I")
                orientation = get_orientation(orientation, "I")
        if not check_distance(current_X, current_y):
            msj = "La coordenada ({}, {}) esta fuera de perimetro".format(current_X, current_y)
            print(msj)
            exit()
        out_list.append({
            'drone_id': drone_id,
            'coord': (current_X, current_y),
            'orientation': orientation
        })
    return out_list


def write_out_file(out_list):
    """
    Write file outN.txt
    :param out_list:
    :return: file
    """
    drone_id = out_list[0]['drone_id']
    file_name = "out" + drone_id + ".txt"
    file = open(file_name, "w+")
    for i in out_list:
        orientation = get_orientation_name(i['orientation'])
        text = "{} direccion {}\n".format(i['coord'], orientation)
        file.write(text)
    file.close()
    print("Archivo creado con exito")
