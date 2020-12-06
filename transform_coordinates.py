import math
def get_distance(x1,y1,x2,y2):
    return math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))



new_files = [
    'VRPNC1m_dist.TXT',
    'VRPNC2m_dist.TXT', 
    'VRPNC3m_dist.TXT',
    'VRPNC4m_dist.TXT',
    'VRPNC5m_dist.TXT',
    'VRPNC11m_dist.TXT',
    'VRPNC12m_dist.TXT'
]

files = [
    'VRPNC1m.TXT',
    'VRPNC2m.TXT', 
    'VRPNC3m.TXT',
    'VRPNC4m.TXT',
    'VRPNC5m.TXT',
    'VRPNC11m.TXT',
    'VRPNC12m.TXT'
]

for index, new_file in enumerate(new_files):
    # 1. Read file
    file = open(files[index],"r+")
    # Remove line breaks and tabs
    file_lines = [
        line.replace("\n","").replace("\t",",") for line in file.readlines()
    ]

    coords_list = []
    # 2. Extracting coordinates spairs
    for coords in file_lines[9:len(file_lines)]:
        sep_coords = coords.split(',')
        parsed_CoorX = int(sep_coords[0])
        parsed_CoorY = int(sep_coords[1])
        parsed_pairs = [parsed_CoorX, parsed_CoorY]
        coords_list.append(parsed_pairs)

    distances = []
    for i in range(len(coords_list)):
        x1 = coords_list[i][0]
        y1 = coords_list[i][1]
        row = []
        for j in range(len(coords_list)):
            x2 = coords_list[j][0]
            y2 = coords_list[j][1]
            row.append(round(get_distance(x1,y1,x2,y2)))
        distances.append(row)


    actual_file = open(new_file, 'w+')
    for text in file_lines[0:8]:
        actual_file.write(text.replace(',',"\t") + '\n')
    actual_file.write('TravelTimes:\n')
    for i in distances:
        for j in range(len(i)):
            if j == len(i)-1:
                actual_file.write('{0}'.format(i[j]))
            else:
                actual_file.write('{0}\t'.format(i[j]))

        actual_file.write('\n')
    actual_file.close()
        