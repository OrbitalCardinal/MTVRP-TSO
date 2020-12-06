import math
import time
import sys

def VRP(filename):
    initial_time = time.time()
    # 1. Read file
    file = open(filename,"r+")
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

    # 4.
    # 3. Extracting demands
    # 5. Demand is saved in a list
    ClientDemands_list = [int(demand) for demand in file_lines[4].split(',')] 

    # 6. Extracting capacity
    VehCapacity = int(file_lines[2].split(" ")[1])

    # 7. Extracting # trips
    nbTrips = int(file_lines[1].split(" ")[1])

    # 8. Trips
    n_trip = 0

    # 9,  Extracting depot coordinates
    depotX, depotY = coords_list[0][0], coords_list[0][1] # 10. Saving depot x coordinate and depot y coordinate
    coords_list.pop(0) # Removing depot coordinates

    clientAngle_dict = []
    # 11. For every coordinate
    for i in range(len(coords_list)):
        x_distance = coords_list[i][0] - depotX # a. calculating x distance to depot
        y_distance = coords_list[i][1] - depotY # b. calculating y distance to depot

        # D. Checking quadrant
        if x_distance > 0  and y_distance > 0 : # l
            calculated_angle = math.atan(abs(y_distance/x_distance))
        if x_distance < 0 and y_distance > 0: # ll
            calculated_angle = 180 - math.atan(abs(y_distance/x_distance))
        if x_distance < 0 and y_distance < 0: # lll
            calculated_angle = 180 + math.atan(abs(y_distance/x_distance))
        if x_distance > 0 and y_distance < 0: # lV
            calculated_angle = 360 - math.atan(abs(y_distance/x_distance))
        # E. Saving client number and calculated angle
        clientAngle_dict.append({'client': i, 'angle' : calculated_angle}) 

    # Sorting angles and client numbers
    clientAngle_dict.sort(key= lambda element: element['angle'])
    clientAngles_matrix = [[element['client'], element['angle']] for element in clientAngle_dict]

    trips = []
    capacity_sum = 0

    visited_clients = []
    for index, client in enumerate(clientAngles_matrix):
        visited_clients.append(client[0])
        capacity_sum += ClientDemands_list[index]
        # 14. Save visited clients and sum the trip
        if capacity_sum >= VehCapacity:
            trips.append({'trip': n_trip, 'visited': visited_clients})
            n_trip += 1
            visited_clients = []
            capacity_sum = 0    
        
        #15. Loop ends when maximum number of trips is exceeded
        if n_trip == nbTrips-1:
            break

    total_cost = 0
    costs_per_trip = []
    for trip in trips:
        actual_trip = trip['visited']

        #Initial distance to depot
        c1x = coords_list[actual_trip[0]][0]
        c1y = coords_list[actual_trip[0]][1]
        depot_cost = math.sqrt(((c1x - depotX) ** 2) + ((c1y - depotY) ** 2))
        costs_per_trip.append(depot_cost)
        # Final distance to depot
        c1x = coords_list[actual_trip[len(actual_trip)-1]][0]
        c1y = coords_list[actual_trip[len(actual_trip)-1]][1]
        depot_cost = math.sqrt(((c1x - depotX) ** 2) + ((c1y - depotY) ** 2))
        costs_per_trip.append(depot_cost)

        # 16. Calculating distances between points
        for i in range(len(actual_trip)-1):
            c1x = coords_list[actual_trip[i]][0]
            c1y = coords_list[actual_trip[i]][1]

            c2x = coords_list[actual_trip[i+1]][0]
            c2y = coords_list[actual_trip[i+1]][1]

            calculated_cost = math.sqrt(((c2x - c1x) ** 2) + ((c2y - c1y) ** 2))
            costs_per_trip.append(calculated_cost)
                
    for i in range(len(costs_per_trip)):
        total_cost += sum(costs_per_trip[0:i+1])

    final_time = time.time()
    total_time = final_time - initial_time



    # 17. printing total cost and execution time
    print("Number of trips = {0}".format(n_trip))
    print("Total cost = {0}".format(total_cost))
    print("Total time = {0}".format(total_time))

files = [
    'VRPNC1m.TXT',
    'VRPNC2m.TXT', 
    'VRPNC3m.TXT',
    'VRPNC4m.TXT',
    'VRPNC5m.TXT',
    'VRPNC11m.TXT',
    'VRPNC12m.TXT'
]
for file in files:
    print(file)
    VRP(file)
    print()




