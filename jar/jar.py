class Jar:
    def __init__(self, capacity=12):
        # Initializing the jar with a default capacity of 12
        if capacity < 0:
            raise ValueError('Wrong capacity')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Returns a string of cookie emojis representing the current size
        return self.size * '🍪'

    def deposit(self, n):
        # Adds cookies to the jar, ensuring it doesn't exceed capacity
        if self.size + n > self.capacity:
            raise ValueError('Exceed capacity')
        self._size += n

    def withdraw(self, n):
        # Removes cookies from the jar, ensuring we don't go below zero
        if self.size < n:
            raise ValueError('There are less cookies than asked to remove')
        self._size -= n

    @property
    def capacity(self):
        # Getter for capacity
        return self._capacity

    @property
    def size(self):
        # Getter for size
        return self._size

def main():
    # Example usage:
    jar = Jar()
    jar.deposit(3)
    print(jar) # Should print 🍪🍪🍪
    jar.withdraw(1)
    print(jar) # Should print 🍪🍪

if __name__ == "__main__":
    main()
