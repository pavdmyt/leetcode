
"""
   Operation   | Running Time
 ----------------------------
  S.enqueue(e) |  O(1)
  S.dequeue()  |  O(1)
  S.first()    |  O(1)
  len(S)       |  O(1)
  S.is_empty() |  O(1)

"""


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'          # streamline memory usage

        def __init__(self, element, next):       # initialize node's fields
            self._element = element              # reference to user's element
            self._next = next                    # reference to next node

    #
    # Queue methods
    #
    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element            # front aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                   # special case as queue is empty
            self._tail = None                 # removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)          # node will be new tail node
        if self.is_empty():
            self._head = newest               # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                   # update reference to tail node
        self._size += 1


class Empty(Exception):
    """Empty ADT."""


def main():
    lq = LinkedQueue()

    print("* Enqueue")
    for e in "abcdefg":
        print(f"enqueue {repr(e)} to queue")
        lq.enqueue(e)
    print(f"* Queue length: {len(lq)}")

    print("\n* dequeue")
    for _ in range(len(lq)):
        e = lq.dequeue()
        print(f"dequeue: {repr(e)}")
    print(f"* Queue length: {len(lq)}")


if __name__ == '__main__':
    main()
