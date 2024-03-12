class Stack:
    EMPTY_SLOT = None

    def __init__(self, size: int):
        self._size = size
        self._stack = [Stack.EMPTY_SLOT] * size
        self._nextFree = 0

    def push(self, item):
        new_item_index = self._nextFree

        if new_item_index >= self._size:
            raise RuntimeError(f"Stack is full ({self._size} items)")

        self._stack[new_item_index] = item
        self._nextFree += 1

        return new_item_index

    def pop(self):
        lastItemIndex = self._nextFree - 1
        removedItem = self._stack[lastItemIndex]

        self._stack[lastItemIndex] = self.EMPTY_SLOT
        self._nextFree -= 1

        return removedItem

    def isFull(self):
        return self._nextFree == self._size

    def isEmpty(self):
        return self._nextFree == 0
    
    def getItems(self):
        return self._stack.copy()

if __name__ == "__main__":
    stack = Stack(5)
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")
    stack.pop()
    print(stack.getItems())