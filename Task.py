class Task:
    def __init__(self, ID, size, a, b, time):
        self.time = time
        self.ID = ID
        self.size = size
        self.a = a
        self.b = b
        self.x = None

    def work(self):
        pass