class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")

        rear = (self.front + self.size) % self.capacity
        self.data[rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.data[self.front]


# Creating a queue with a capacity of 3
printer = Queue(3)

print(printer.is_empty())  # True

printer.enqueue("Report.pdf")
printer.enqueue("Photo.png")
printer.enqueue("Notes.docx")

print(printer.is_full())  # True
print(printer.peek())     # Report.pdf

print(printer.dequeue())  # Report.pdf
print(printer.dequeue())  # Photo.png

printer.enqueue("Invoice.pdf")

print(printer.peek())     # Notes.docx
print(printer.is_full())  # False