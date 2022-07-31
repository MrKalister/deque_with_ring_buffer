class EmptyList(Exception):
    """Called if use methods pop_back or pop_front and list is empty."""

    pass


class FullList(Exception):
    """Called if use methods push_back or push_front and list is full."""

    pass


class Deque:
    """Class double ended queue."""

    def __init__(self, max_size: int) -> None:
        """
        Is works on the principle of a ring buffer.

        deque - list the size defined by the parameter max_size
        head is start list,
        tail is end list,
        size is current size of list.
        """
        self._deque = [None] * max_size
        self._max_size = max_size
        self._head = 0
        self._tail = 0
        self._size = 0

    def is_empty(self) -> bool:
        """Check size of list."""
        return self._size == 0

    def push_front(self, item: int) -> None:
        """Add element in start list."""
        if self._size == self._max_size:
            raise FullList
        if self.is_empty():
            self._tail = (self._tail + 1) % self._max_size
        self._deque[self._head] = item
        self._head = (self._head - 1) % self._max_size
        self._size += 1

    def push_back(self, item: int) -> None:
        """Add element in end list."""
        if self._size == self._max_size:
            raise FullList
        if self.is_empty():
            self._head = (self._head - 1) % self._max_size
        self._deque[self._tail] = item
        self._tail = (self._tail + 1) % self._max_size
        self._size += 1

    def pop_back(self) -> int:
        """Pick an item from the ending of the list."""
        if self.is_empty():
            raise EmptyList
        self._tail = (self._tail - 1) % self._max_size
        item = self._deque[self._tail]
        self._deque[self._tail] = None
        self._size -= 1
        if self._size == 0:
            self._tail = 0
            self._head = 0
        return item

    def pop_front(self) -> int:
        """Pick an item from the beginning of the list."""
        if self.is_empty():
            raise EmptyList
        self._head = (self._head + 1) % self._max_size
        item = self._deque[self._head]
        self._deque[self._head] = None
        self._size -= 1
        if self._size == 0:
            self._tail = 0
            self._head = 0
        return item


def deque_with_ring_buffer() -> None:
    """
    Pass the amount of commands and the object.

    The function executes the methods of the object that the user enters.
    """
    amount_commands = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for _ in range(amount_commands):
        command, *arguments = input().split()
        if not arguments:
            try:
                print(getattr(deque, command)())
            except EmptyList:
                print('error')
        else:
            try:
                getattr(deque, command)(*arguments)
            except FullList:
                print('error')


if __name__ == '__main__':
    deque_with_ring_buffer()
