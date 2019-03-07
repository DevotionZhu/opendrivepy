

class OpenDrive(object):
    def __init__(self):
        self.header = None
        self.roads = dict()
        self.controllers = list()
        self.junctions = dict()
        self.junction_groups = list()
        self.stations = list()

    def left_most_endpoint(self):
        if self.roads is not None:
            leftmost = self.roads[0].predecessor
            for road in self.roads.values():
                if road.predecessor.x < leftmost.x:
                    leftmost = road.predecessor
                if road.successor.x < leftmost.x:
                    leftmost = road.successor

            return leftmost

        return None
