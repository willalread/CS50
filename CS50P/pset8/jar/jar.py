class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-nagative int")
        self.capacity = capacity

    def __str__(self):
        return "🍪"*self.n

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    size =

if __name__ == "__main__":
    main()
