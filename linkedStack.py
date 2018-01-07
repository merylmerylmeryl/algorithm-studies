class LinkedStack:
    """LIFO Stack class as a singly-linked list"""
    class Node:
        """Lightweight node class representing an item in the list"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Creates an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add a new element as the head of the list"""
        self._head = Node(e, self._head)
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO)

        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        return answer
        
        self._size -= 1


if __name__ == '__main__':
    print('poop')
        
