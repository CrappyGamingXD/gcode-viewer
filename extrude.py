class extrude:
    x = [0,0]
    y = [0,0]
    z = [0,0]
    e = 0
    feedrate = 0
    temperature = 0
    fan = 0

    def __init__(self, x, y, z, e, feedrate, temperature, fan):
        self.x = x
        self.y = y
        self.z = z
        self.e = e
        self.feedrate = feedrate
        self.temperature = temperature
        self.fan = fan
