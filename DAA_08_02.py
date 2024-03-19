MAX_SIZE = 100

class Stack:
    def __init__(self):
        self.data = [0] * MAX_SIZE
        self.top = -1

    def push(self, item):
        if self.top >= MAX_SIZE - 1:
            return False  # Stack overflow
        self.top += 1
        self.data[self.top] = item
        return True

    def pop(self):
        if self.top < 0:
            return None, False  # Stack underflow
        item = self.data[self.top]
        self.top -= 1
        return item, True

    def is_empty(self):
        return self.top == -1

    def print_elements(self):
        print("Elements in stack:")
        for i in range(self.top, -1, -1):
            print(self.data[i])

class Queue:
    def __init__(self):
        self.data = [0] * MAX_SIZE
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % MAX_SIZE == self.front:
            return False  # Queue full
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % MAX_SIZE
        self.data[self.rear] = item
        return True

    def dequeue(self):
        if self.front == -1:
            return None, False  # Queue empty
        item = self.data[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % MAX_SIZE
        return item, True

    def is_empty(self):
        return self.front == -1

    def print_elements(self):
        print("Elements in queue:")
        if self.front == -1:
            print("Queue is empty")
        elif self.front <= self.rear:
            for i in range(self.front, self.rear + 1):
                print(self.data[i])
        else:
            for i in range(self.front, MAX_SIZE):
                print(self.data[i])
            for i in range(self.rear + 1):
                print(self.data[i])

class LinkedList:
    def __init__(self):
        self.data = [None] * MAX_SIZE
        self.head = -1
        self.next_available = 0
        for i in range(MAX_SIZE - 1):
            self.data[i] = i + 1
        self.data[MAX_SIZE - 1] = None

    def insert(self, item):
        if self.next_available is None:
            return False  # List full
        new_node_index = self.next_available
        self.next_available = self.data[new_node_index]
        self.data[new_node_index] = (item, self.head)
        self.head = new_node_index
        return True

    def remove(self):
        if self.head == -1:
            return None, False  # List empty
        item, next_head = self.data[self.head]
        self.data[self.head] = self.next_available
        self.next_available = self.head
        self.head = next_head
        return item, True

    def is_empty(self):
        return self.head == -1

    def print_elements(self):
        print("Elements in linked list:")
        current = self.head
        while current != -1:
            item, next_index = self.data[current]
            print(item)
            current = next_index

# Sample input/output for stack
if __name__ == "__main__":
    print("Stack:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Pop:", stack.pop())  # Output: 3
    print("Pop:", stack.pop())  # Output: 2
    print("Is empty:", stack.is_empty())  # Output: False
    stack.print_elements()  # Output: Elements in stack: 1

    # Sample input/output for queue
    print("\nQueue:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Dequeue:", queue.dequeue())  # Output: 1
    print("Dequeue:", queue.dequeue())  # Output: 2
    print("Is empty:", queue.is_empty())  # Output: False
    queue.print_elements()  # Output: Elements in queue: 3

    # Sample input/output for singly linked list
    print("\nSingly Linked List:")
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    print("Remove:", linked_list.remove())  # Output: 3
    print("Remove:", linked_list.remove())  # Output: 2
    print("Is empty:", linked_list.is_empty())  # Output: False
    linked_list.print_elements()  # Output: Elements in linked list: 1
