from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class ContainsLoopError(Exception):
    pass

class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next_node: Node | None = None

    def __iter__(self) -> Iterator[Any]:
        node = self
        visited = set()
        while node:
            if node in visited:
                raise ContainsLoopError
            visited.add(node)
            yield node.data
            node = node.next_node

       @property
    def has_loop(self) -> bool:
        """
        Check whether the linked list contains a cycle.

        Uses Floyd's cycle detection algorithm with O(1) extra space.

        >>> root_node = Node(1)
        >>> root_node.next_node = Node(2)
        >>> root_node.next_node.next_node = Node(3)
        >>> root_node.has_loop
        False

        >>> root_node.next_node.next_node.next_node = root_node
        >>> root_node.has_loop
        True

        >>> single_node = Node(1)
        >>> single_node.next_node = single_node
        >>> single_node.has_loop
        True

        >>> duplicate_nodes = Node(5)
        >>> duplicate_nodes.next_node = Node(5)
        >>> duplicate_nodes.has_loop
        False
        """
        slow = self
        fast = self

        while fast is not None and fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node.next_node

            if slow is fast:
                return True

        return False

if __name__ == "__main__":
    root_node = Node(1)
    root_node.next_node = Node(2)
    root_node.next_node.next_node = Node(3)
    root_node.next_node.next_node.next_node = Node(4)
    print(root_node.has_loop)  # False
    root_node.next_node.next_node.next_node = root_node.next_node
    print(root_node.has_loop)  # True

    root_node = Node(5)
    root_node.next_node = Node(6)
    root_node.next_node.next_node = Node(5)
    root_node.next_node.next_node.next_node = Node(6)
    print(root_node.has_loop)  # False

    root_node = Node(1)
    print(root_node.has_loop)  # False
