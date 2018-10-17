# Handy Freight Class calculator written in Python.
# Takes the dimensions of multiple parcels or
# pallets and calculates the combined freight class.


def get_freight_class(density):
    if density < 1:
        return 500
    elif density < 2:
        return 400
    elif density < 3:
        return 300
    elif density < 4:
        return 250
    elif density < 5:
        return 200
    elif density < 6:
        return 175
    elif density < 7:
        return 150
    elif density < 8:
        return 125
    elif density < 9:
        return 110
    elif density < 10.5:
        return 100
    elif density < 12:
        return 92.5
    elif density < 13.5:
        return 85
    elif density < 15:
        return 77.5
    elif density < 22.5:
        return 70
    elif density < 30:
        return 65
    elif density < 35:
        return 60
    elif density < 50:
        return 55
    else:
        return 50


def get_lbs_vol_density():
    dictionary = {}
    for piece in range(1, num_pieces + 1):
        print("*" * 25)
        length = float(input("What is the length of piece {}? ".format(piece)))
        width = float(input("What is the width of piece {}? ".format(piece)))
        height = float(input("What is the height of piece {}? ".format(piece)))
        cu_ft = (length * width * height) / 1728

        dictionary["piece{}_cu_ft".format(piece)] = cu_ft
    return dictionary


def get_total_volume(dict):
    total_vol = 0
    for piece in range(1, num_pieces + 1):
        total_vol += dict["piece{}_cu_ft".format(piece)]
    return float(total_vol)


def get_total_weight(dict):
    total_weight = 0
    for piece in range(1, num_pieces + 1):
        total_weight += dict["piece{}_weight".format(piece)]
    return float(total_weight)

if __name__ == "__main__":
    while True:
        # Prompts user for number of pieces
        num_pieces = int(input("How many total pieces in this shipment? "))
        total_vol = get_total_volume(get_lbs_vol_density())
        print("*" * 25)
        total_weight = float(input("What is the total weight of this shipment? "))
        total_density = total_weight / total_vol
        print("*" * 25)
        print("Freight class is {}".format(get_freight_class(total_density)))
        print("Total volume is {} cubic feet".format(round(total_vol, 2)))
        print("Total weight is {} lbs".format(round(total_weight, 2)))
        print("*" * 25)
