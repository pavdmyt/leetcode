
"""
   Operation   | Running Time
 ----------------------------
  S.push(e)    |  O(1)
  S.pop()      |  O(1)
  S.top()      |  O(1)
  len(S)       |  O(1)
  S.is_empty() |  O(1)

"""


class LinkedStack:
    """LIFO Stack implementation using a singly linked list storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'          # streamline memory usage

        def __init__(self, element, next):       # initialize node's fields
            self._element = element              # reference to user's element
            self._next = next                    # reference to next node

    #
    # Stack methods
    #
    def __init__(self):
        """Create an empty stack."""
        self._head = None                        # reference to the head node
        self._size = 0                           # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)   # create and link a new node
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element            # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next         # bypass the former top node
        self._size -= 1
        return answer


class Empty(Exception):
    """Empty ADT."""


def main():
    ls = LinkedStack()

    print("* Pushing")
    for e in "abcdefg":
        print(f"push {repr(e)} to stack")
        ls.push(e)
    print(f"* Stack length: {len(ls)}")

    print("\n* Popping")
    for _ in range(len(ls)):
        e = ls.pop()
        print(f"pop: {repr(e)}")
    print(f"* Stack length: {len(ls)}")


if __name__ == '__main__':
    main()
