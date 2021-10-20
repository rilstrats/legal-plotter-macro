import re
import pyautogui
pyautogui.FAILSAFE = True

def get_number(prompt,blank_entry=False):
    # Retrieves a number from a user and validates it.
    while True:
        user_number = input (prompt)
        if blank_entry and user_number=="":
            return user_number
        else:
            try:
                user_number = int (user_number)
                return user_number
            except:
                print ("Please enter a valid number.")


def get_legal():
    # Take user input of legal description
    print ("\nPlease copy and paste a legal description.")
    print ("Ensure that there isn't any extra ENTER lines in this description,") 
    print ("as these will cause the program to crash.")
    legal = input ("")
    legal = legal.upper()
    return legal


def format_legal(legal):
    # Finds splitting key words and replaces them with (something), then splits where (something) is.
    # Then recombines curves. Why are curves formatted so weird? 
    # Finally removes sections without any information.
    legal = legal.replace (",", " ")
    legal = re.sub(r"\bBEG\b|\bBEGINNING\b", ";", legal)
    legal = re.sub(r"\bTH\b|\bTHENCE\b", ";", legal)
    legal = re.sub(r"\bAND\b", ";", legal)
    legal = re.sub(r"; ;|;;", r";", legal)

    legal = re.sub(r"(?P<bearing>[0-9][0-9]*[.*°'\"][0-9][0-9]*[*°'\"][0-9][0-9]*[*°'\"])", r" \g<bearing> ",legal)
    legal = re.sub(r"(?P<before>\bCUR\b[^;]*|\bCURVE\b[^;]*);*(?P<after>[^;]*\bCUR\b|[^;]*\bCURVE\b)", r"\g<before> \g<after>", legal)
    
    legal_list = legal.split(";") 
    print (legal_list)
    for segment in legal_list:
        if not re.search(r"[0-9][0-9]*[.*°'\"][0-9][0-9]*", segment):
            legal_list.pop(legal_list.index(segment))
    return(legal_list)


def define_segments(legal_list):

    master_list =[]
    for segment in legal_list:
        if re.search(r"\b(?:CUR|CURVE)\b", segment):
            master_list.append(define_curve(segment))
        else:
            master_list.append(define_line(segment))
    
    return master_list


def define_line(segment):
    
    line = re.search(r"\b(?P<n_s>N|NORTH|S|SOUTH)\s*(?P<degrees>\d*)[.*°'\"](?P<minutes>\d*)[*°'\"](?P<seconds>\d*)[*°'\"]\s*(?P<e_w>E|EAST|W|WEST)\b\D*(?P<distance>\d*[.]\d*)\s*(?:'|FT|FEET)", segment)

    try:
        bearing = line.group("degrees") + "." + line.group("minutes") + line.group("seconds")
    except:
        print (f"\nProgram failed to determine line bearing from '{segment}'")

    try:
        n_s = line.group("n_s")
        e_w = line.group("e_w")

        if n_s == "N" or n_s == "NORTH":
            if e_w == "E" or e_w == "EAST":
                quadrant = "1"
            elif e_w == "W" or e_w == "WEST":
                quadrant = "4"
        elif n_s == "S" or n_s == "SOUTH":
            if e_w == "E" or e_w == "EAST":
                quadrant = "2"
            elif e_w == "W" or e_w == "WEST":
                quadrant = "3"
    except:
        print (f"\nProgram failed to determine line quadrant from '{segment}'")


    try:
        distance = line.group("distance")
        distance = distance.strip()
    except:
        print (f"\nProgram failed while trying to determine line distance from '{segment}'")

    try:
        return ["line", quadrant, bearing, distance]
    except:
        print (f"\nProgram failed to determine all line info for {segment}")


def define_curve(segment):

    try:
        m_radius = re.search(r"\s*(?P<radius>[0-9]*[.][0-9]*)\s*(?:FT|FEET|FOOT)\s*\b(?:RAD|RADIUS)\b.*\b(?P<direction>RT|RIGHT|LT|LEFT)\b", segment)
        radius = m_radius.group("radius")
        direction = m_radius.group("direction")
        if direction == "LT" or direction == "LEFT":
            radius = "-" + radius
    except:
        print (f"\nProgram failed to determine curve radius from '{segment}'")

    try:
        m_length = re.search(r"(?:ALG|ALONG)\D*(?P<arc_length>\d*[.]\d*)", segment)
        m_chord = re.search(r"(?:CHD|CHORD)\D*(?:\d*[.*°'\"]\d*[*°'\"]\d*[*°'\"])\D*(?P<chord_length>\d*[.]\d*)", segment)
        if m_length:
            extra_type = "l"
            extra_info = m_length.group("arc_length")
        elif m_chord:
            extra_type = "c"
            extra_info = m_length.group("chord_length")
    except:

        print(f"\nProgram failed to determine additional curve info from '{segment}'")
    try:
        return ["curve", "r", radius, extra_type, extra_info]
    except:
        print (f"Program failed to determine all curve info for {segment}")
  

def display_legal(master_list):
    while True:
        print ("")
        for segment in master_list:
            try:
                if segment[0] == "line":
                    print (f"{master_list.index(segment):>3}{segment[0]:>8}{segment[1]:>4}{segment[2]:>10}{segment[3]:>15}")
                if segment[0] == "curve":
                    print (f"{master_list.index(segment):>3}{segment[0]:>8}{segment[1]:>4}{segment[2]:>10}{segment[3]:>4}{segment[4]:>11}")
            except:
                print (f"Failed to display segment {master_list.index(segment)}: {segment}")

        print ()
        print ("From here, you can: ")
        print ("    1) Edit a Segment")
        print ("    2) Delete a Segment")
        print ("    3) Plot the List")
        print ("    4) Cancel Plotting")
        choice = get_number("What would you like to do? (Type the number next to the option): ")
        if choice == 1:
            user_number = get_number("Please type the segment number you would like to edit: ")
            print (master_list[user_number])
            print ("Type what you would like to replace this with, in the same format.")
            print ("(Ex: 'line,3,35.5642,653.12'")
            replacement = input("")
            replacement = replacement.split(",")
            master_list[segment] = replacement
        elif choice == 2:
            segment_choice= get_number("Please type the segment number you would like to delete: ")
            while True:
                delete_it = input(f"Are you sure you would like to delete segment {segment_choice}: {master_list[segment]}? (YES or NO): ")
                if delete_it.upper() == "YES":
                    master_list.pop(segment)
                    break
                elif delete_it.upper() == "NO":
                    break
        elif choice == 3:
            type_speed = get_number("How fast would you like to type? (Leave blank to use default value '0.1' seconds): ",blank_entry=True)
            if type_speed == "":
                type_speed=0.1
            enter_speed = get_number("How fast would you like to press enter? (Leave blank to use default '0.2' seconds): ",blank_entry=True)
            if enter_speed == "":
                enter_speed=0.2
            plot_legal(master_list)
        elif choice == 4:
            quit()


def plot_legal(master_list,type_speed,enter_speed):
    # Uses PyAutoGUI to select the AutoCAD window and plot the lines and curves

    previous_plot = ""

    for segment in master_list:
        try:
            if segment[0] == "line":
                if previous_plot != "line":
                    print ("\nPlease select CREATE LINE BY BEARING, \nthen select starting point or end of previous curve.")
                    print ("If ready, Civil 3D should be waiting for quadrant specification.")
                    input("Once ready put cursor at the end of this sentence, \nhover mouse over Civil 3D, \nand press ENTER. ")
                    pyautogui.click()

                plot(segment, master_list.index(segment))
                
                previous_plot = "line"

            elif segment[0] == "curve":

                print ("\nPlease select CREATE CURVE FROM END OF OBJECT, \nthen select end of previous line or curve.")
                print ("If ready, Civil 3D should be waiting for radius or point entry.")
                input("Once ready put cursor at the end of this sentence, \nhover mouse over Civil 3D, \nand press ENTER. ")
                pyautogui.click()
                
                plot(segment, master_list.index(segment))

                previous_plot = "curve"

        except:
            print (f"\nUnable to plot segment {master_list.index(segment)}: {segment}")

        
    
    print ("\nLegal plotting was successful!")


def plot(segment, index):
    for info in segment:
        try:
            if info == "line" or info == "curve":
                print()
            else:
                pyautogui.write(info, interval=0.1)
                pyautogui.write("\n", interval=0.2)
                print(info)
        except: 
            print (f"Failed to plot {info} from segment {index}: {segment}")


def main():
    legal = get_legal()
    legal_list = format_legal(legal)
    master_list = define_segments(legal_list)
    display_legal(master_list)
    print()
    pass


main()