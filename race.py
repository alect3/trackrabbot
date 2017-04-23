CheckPoint = namedtuple('CheckPoint', ['time', 'distance'])

class Race:
    def __init__(self, name, distance, time, checkpoints):
        self.name = name
        self.distance = distance
        self.time = time
        self.checkpoints = map(CheckPoint._make, checkpoints) 
        self.current_checkpoint = 0

    def get_next_checkpoint(self, current_distance):
        if len(self.checkpoints) = 0: return None
        while self.checkpoints[self.current_checkpoint].distance < d:
            self.current_checkpoint += 1 
            if self.current_checkpoint >= len(self.checkpoints): return None
        return self.checkpoints[self.current_checkpoint]
