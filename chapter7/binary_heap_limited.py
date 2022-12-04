from binary_heap import BinaryHeap

class BinaryHeapLimited(BinaryHeap):
    def __init__(self, size):
        super().__init__()
        self.size = size 

    def insert(self, item):
        super().insert(item)
        self._heap = self._heap[:self.size]
        