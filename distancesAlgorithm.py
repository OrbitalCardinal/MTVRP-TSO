def distancesVRP(file):
    import time
    initial_time = time.time()
    # 1. Read file
    file = open(file,"r+")
    file_lines = [line.replace("\n","").replace("\t",",") for line in file.readlines()]
    # print(file_lines)
    # 1. Parsing and saving matrix distances
    unparsed_matrix = [row.split(",") for row in file_lines[8:]]
    distances =[]
    for i in unparsed_matrix:
        row = []
        for j in i:
            row.append(int(j))
        distances.append(row)
    # print(distances)


    # 2. Parsing and saving client demands
    ClientDemands = [int(n) for n in file_lines[4].split(",")]
    # print(ClientDemands)

    # 3. Parsing vehicle capacity and saving it
    VehCapacity = int(file_lines[2].split(" ")[1])
    # print(VehCapacity)

    # 4. Parsing and saving # trips
    max_trips = int(file_lines[1].split(' ')[1])
    # print(max_trips)

    # 5. Creating variables
    n_trips = 0
    indicator = 0
    minimum = 0
    cost = 0
    demand = 0
    minimum_index = 0
    enters = True

    # 6. Creating visited empty list
    visited = []

    # 7
    visited.append(0)

    # 8.
    while n_trips <= max_trips and len(visited) <= len(ClientDemands):

        # 9.
        if indicator < len(ClientDemands) - 1:
            minimum = distances[indicator][indicator+1]
        else:
            minimum - distances[indicator][indicator-1]
        
        # 10.
        for i in range(len(ClientDemands)):
            enters = True # A.
            d = distances[indicator][i] # B.

            # C.
            for dato in visited:
                if i == dato: # a.
                    enters = False # b.
            # D.
            if enters:
                if distances[indicator][i] < minimum:
                    minimum = distances[indicator][i]
                    minimum_index = i
        cost = cost + minimum
        demand = demand + ClientDemands[minimum_index - 1]
        if demand > VehCapacity:
            n_trips += 1
            demand = 0
            indicator = 0
        else:
            visited.append(minimum_index)
            indicator = minimum_index
    # print("Total cost = {0}".format(cost))
    acumulated_costs = []
    for i in range(len(visited)):
        acumulated_costs.append(distances[i][visited[i]])
    total_cost = 0
    for i in range(len(acumulated_costs)):
        total_cost += sum(acumulated_costs[0:i+1])
    final_time = time.time()
    total_time = final_time - initial_time
    print("Total cost = {0}".format(total_cost))
    print("Execution time = {0}".format(total_time))

files = [
    'MT-DMP10s0-01.txt',
    'MT-DMP10s0-05.txt',
    'MT-DMP15s0-03.txt',
    'MT-DMP15s0-04.txt',
    'VRPNC1m_dist.TXT',
    'VRPNC2m_dist.TXT', 
    'VRPNC3m_dist.TXT',
    'VRPNC4m_dist.TXT',
    'VRPNC5m_dist.TXT',
    'VRPNC11m_dist.TXT',
    'VRPNC12m_dist.TXT'
]

for file in files:
    print(file)
    distancesVRP(file)
    print()