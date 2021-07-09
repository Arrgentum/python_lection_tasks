def turtle(coord, direction):
    coord = list(coord)
    while True:
        y = yield coord
        if (y == "r" and direction == 0) or (y == "l" and direction == 2):
            direction = 3
        elif (y == "r" and direction == 3) or (y == "l" and direction == 1):
            direction = 2
        elif (y == "r" and direction == 2) or (y == "l" and direction == 0):
            direction = 1
        elif (y == "r" and direction == 1) or (y == "l" and direction == 3):
            direction = 0
        elif y == "f":
            if direction == 0:
                coord[0] += 1
            elif direction == 1:
                coord[1] += 1
            elif direction == 2:
                coord[0] -= 1
            elif direction == 3:
                coord[1] -= 1
