import re

legal1 = 'NORTH 0\'14\'54" EAST, ALONG THE LOT LINE, 211.50 FEET'
m_bearing = re.search(r'[0-9]*[*°\'"]([0-9][0-9][*°\'"])*[0-9][0-9][*°\'"]', legal1)
bearing = m_bearing.group(0)
new_legal = re.sub(bearing," ", legal1)
print (bearing, new_legal)


legal2 = 'N0°14\'54"E, ALONG THE LOT LINE, 211.50\''


"""
Old code
def split_legal_description(legal):
    # Split legal description into list based on thence calls
    # return thence_list
    legal = legal.upper()
    legal_list = legal.split("THENCE")
    legal_list[0] = legal.split("RUNNING")
    return legal_list
    


def define_line_info(thence_call):
    # Calls the find_quadrant, find_bearing, and find_distance functions and stores them in a list
    # Also returns this list to a master list with all information

    def define_quadrant(thence_call):
        # Finds quadrant and returns it to store in a list
        # for word in thence_list:
        if "NORTH" in thence_list or "N" in thence_list or "NORTH," in thence_list or "N," in thence_list:
            if "EAST" in thence_list or "E" in thence_list or "EAST," in thence_list or "E," in thence_list:
                quadrant = "1"
            elif "WEST" in thence_list or "W" in thence_list or "WEST," in thence_list or "W," in thence_list:
                quadrant = "4"
        elif "SOUTH" in thence_list or "S" in thence_list or "SOUTH," in thence_list or "S," in thence_list:
            if "EAST" in thence_list or "E" in thence_list or "EAST," in thence_list or "E," in thence_list:
                quadrant = "2"
            elif "WEST" in thence_list or "W" in thence_list or "WEST," in thence_list or "W," in thence_list:
                quadrant = "3"

        return quadrant


    def define_bearing(thence_call):
        # Finds bearing and returns it to store in a list
        m_bearing = re.search(r'[0-9]*[*°\'"]([0-9][0-9][*°\'"])*[0-9][0-9][*°\'"]', thence_call)
        bearing = m_bearing.group(0)
        new_legal = re.sub(bearing," ", legal1)
        print (bearing, new_legal)

        return bearing


    def define_distance():
        # Finds distance and returns it to store in a list
        return distance

    import re

    line_info_list = ["line"]

    
    # quadrant = define_quadrant(thence_list)
    bearing = define_bearing(thence_call)
    print (bearing)
    # distance = define_distance(thence_list)

    # line_info_list.append(quadrant)
    # line_info_list.append(bearing)
    # line_info_list.append(distance)
    print (line_info_list)
    #return line_info_list


def define_curve_info(thence_call):
    # Calls the define_radius, and define_extra functions and stores them in a list
    # Also returns this list to a master list with all information

    def define_radius(thence_call):
        # Finds radius and returns it to store it in a list
        return radius

    def define_extra_type(thence_call):
        # Finds extra type, defines type of extra (tangent, chord, delta, length, or external)
        # Also, returns it to store in list
        return extra_type

    def define_extra_info(thence_call, extra_type):
        # Finds extra info and returns it to store in a list
        return extra_info
"""