class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.current = None

    def append(self, item):
        if len(self.buffer) == self.capacity:
            self.buffer[self.current] = item
            self.current = (self.current +1) % self.capacity
        else:
            self.buffer.append(item)
            if len(self.buffer) == self.capacity:
                self.current = 0

    def get(self):
        return self.buffer