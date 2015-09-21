# Convert from Order to Path
def convertOTP(order) :
    path = [0 for i in range(len(order))]
    city = [n for n in range(len(order))]

    for i in range(len(order)):
        path[i] = city[order[i]]
        city.pop(order[i])

    return path[:]
