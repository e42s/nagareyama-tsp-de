# Convert from Order to Path
def convertOTP(order) :
    tmp = []

    for i in range(len(order)):
        if order[i] >= 0 and order[i] <= len(order) - 1 - i:
            tmp.append(order[i])
        elif order[i] < 0:
            tmp.append(0)
        elif order[i] > len(order) - 1 - i:
            tmp.append(len(order) - 1 - i)

    path = [0 for i in range(len(order))]
    city = [n for n in range(len(order))]
    for i in range(len(tmp)):
        path[i] = city[tmp[i]]
        city.pop(tmp[i])

    return path[:]

# Convert from Path to Order
def convertPTO(inds , len_dat , path , order):

    for i in range(inds):
        city = [n for n in range(len_dat)]
        for j in range(len(city)):
            order[i , j] = city.index(path[i , j])
            city.pop(city.index(path[i , j]))

    return order
