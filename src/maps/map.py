# map.py
class Map:
    def __init__(self, map_file):
        self.tiles = self.load_map(map_file)

    def load_map(self, map_file):
        with open(map_file, 'r') as file:
            return [[int(char) for char in line.split()] for line in file]