
def calculate_distance():
    print('Welcome to the coordinate distance Calculator!')
    print('Please enter the x & y coordinates of your two data points, followed by the distance type')
    while True:
        try:
            x1 = float(input("x1: "))
            y1 = float(input("y1: "))
            x2 = float(input("x2: "))
            y2 = float(input("y2: "))
            break
        except ValueError:
            print('Please make sure your coordinates are of type integer or float')


    dist_type = input("Distance Type (enter E for Euclidean or M for Manhattan): ")
    dist_type_dict = {'E': 'Euclidean', 'M': 'Manhattan'}

    if dist_type is 'E':
        dist = ( (x1 - x2)**2 + (y1 - y2)**2)**0.5
    elif dist_type is 'M':
        dist = abs(x1 - x2) + abs(y1 - y2)
    else:
        print('Please make sure distance types are entered correctly. Enter E for Euclidean or M for Manhattan')

    print(f'\n{dist_type_dict[dist_type]} distance of your co-ordinates {x1, y1} & {x2, y2} is {round(dist,2)}')



if __name__ == "__main__":
    calculate_distance()