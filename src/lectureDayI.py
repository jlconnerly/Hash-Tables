class DynamicArray:
    # my_array = [4] # Make an empty array of size 4
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):

        if self.count >= self.capacity:
            self.double_size()
            print("Error array is full")

        # make sure index is in range
        if index > self.count:
            print("Error index is out of range")
            return
            # Shift everything over to right
            # Start with the last one
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

            # insert out value
        self.storage[index] = value
        self.count += 1
    
    def append(self, value):
        self.insert(self.count, value)

    def double_size(self):
        self.capacity *= 2
        new_stroage = [None] * self.capacity
        for i in range(self.count):
            new_stroage[i] = self.storage[i]

        self.storage = new_stroage

my_array = DynamicArray(4)
my_array.insert(0, 1)
my_array.insert(0, 2)
my_array.insert(1, 3)
my_array.insert(3, 4)
my_array.insert(0, 5)
print(my_array.storage)