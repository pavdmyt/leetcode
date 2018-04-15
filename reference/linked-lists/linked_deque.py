from doubly_linked_list import _DoublyLinkedBase


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element       # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element      # real item just before trailer

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)  # after header

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)


class Empty(Exception):
    """Empty ADT."""


def main():
    ld = LinkedDeque()

    print("* Insert first")
    for e in "abcdef":
        print(f"inserting {repr(e)} to deque head")
        ld.insert_first(e)
    print(f"* Deque length: {len(ld)}")

    print("\n* Delete first")
    for _ in range(len(ld) // 2):
        e = ld.delete_first()
        print(f"deleting: {repr(e)}")
    print(f"* Deque length: {len(ld)}")

    print("\n* Delete last")
    for _ in range(len(ld)):
        e = ld.delete_last()
        print(f"deleting: {repr(e)}")
    print(f"* Deque length: {len(ld)}")


if __name__ == '__main__':
    main()
