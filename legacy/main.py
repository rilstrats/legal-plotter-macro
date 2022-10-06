"""
try:
            m_bearing = re.search(r"\w\s*(?P<degrees>[0-9]*)[.*°'\"](?P<minutes>[0-9][0-9])[*°'\"](?P<seconds>[0-9][0-9])[*°'\"]\s*\w", segment)
            bearing = m_bearing.group("degrees") + "." + m_bearing.group("minutes") + m_bearing.group("seconds")
        except:
            print (f"\nProgram failed while trying to determine line bearing from '{segment}'")
            print ("If possiblec fix the error and try again.")

        try:
            quad = re.search(r"\b(?P<n_s>N|NORTH|S|SOUTH)\b\s*\b(?P<e_w>E|EAST|W|WEST)\b", segment)

            n_s = quad.group("n_s")
            e_w = quad.group("e_w")

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
            print (f"\nProgram failed while trying to determine line quadrant from '{segment}'")
            print ("If possible, fix the error and try again.")


        try:
            m_distance = re.search(r"\s*(?P<distance>[0-9]*[.][0-9]*)\s*(?:'|FT|FEET)", segment)
            distance = m_distance.group("distance")
            distance = distance.strip()
        except:
            print (f"\nProgram failed while trying to determine line distance from '{segment}'")
            print ("If possible, fix the error and try again.")

        try:
            return ["line", quadrant, bearing, distance]
        except:
            print (f"Program failed to determine all line info for {segment}")
"""


"""
            line =  re.search(r"(?P<n_s>\s*N\s*|\s*NORTH\s*|\s*S\s*|\s*SOUTH\s*)(?P<degrees>[0-9]*)[.*°'\"](?P<minutes>[0-9][0-9])[*°'\"](?P<seconds>[0-9][0-9])[*°'\"](?P<e_w>\s*E\s*|\s*EAST\s*|\s*W\s*|\s*WEST\s*)[^0-9]*(?P<distance>\s*[0-9]*[.][0-9]*\s*)('|FT|FEET)", thence_call)
            
            bearing = line.group("degrees") + "." + line.group("minutes") + line.group("seconds")
            bearing = bearing.strip()
            
            n_s = line.group("n_s")
            n_s = n_s.strip()

            e_w = line.group("e_w")
            e_w = e_w.strip()

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

            distance = line.group("distance")
            distance = distance.strip()

            print("line", quadrant, bearing, distance)
"""