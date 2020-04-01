## Imports
import numpy as np


class Qtable():
    def __init__(self, json_data, responses):
        # TODO: process json_data to define Q matrix dims - should be 3d:
        #  [engineering, sales, product] x [type, description, price] x [potential responses]

