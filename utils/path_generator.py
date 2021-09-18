import random
import numpy as np
import math

import utils.convex_hull as ch
import utils.linear_transformations as lt
from utils import constants

def generate_convex_polygon():
    #? Guarantees that we will have car in our convex polygon
    coords = [(constants.CAR_POS_X, constants.CAR_POS_Y + 10)]
    num_of_points = 20

    for i in range (num_of_points):
        x = random.randrange(constants.LEFT_SCREEN_WIDTH)
        y = random.randrange(constants.SCREEN_HEIGHT)
        coords.append((x, y))

    coords1 = ch.gift_wrap(coords)

    scaling_factor = 0.6
    offset_x = 200
    offset_y = 150
    coords2 = lt.apply_scaling(scaling_factor, scaling_factor, coords1)
    coords2 = lt.apply_translation(offset_x, offset_y, coords2)

    polygon = [coords1, coords2]

    is_closed = True
    return polygon, is_closed

def main():
    pass

if __name__ == '__main__':
    main()
    
