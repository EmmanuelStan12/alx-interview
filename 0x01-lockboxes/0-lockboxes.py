#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of keys): A list of boxes each containing keys

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    queue = deque([0])
    visited = {0}
    return traverse(boxes, queue, visited)

def traverse(boxes, queue, visited):
    """
    Traverse the boxes using keys and a queue

    Args:
        boxes (list of list of int): A list of boxes, each containing keys.
        queue (deque): A deque used to track the boxes to process.
        visited (set): A set of boxes that have been visited.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    while queue:
        index = queue.popleft()
        if index not in visited:
            visited.add(index)

        for key in boxes[index]:
            if key not in visited and 0 <= key < len(boxes):
                queue.append(key)

        if len(boxes) == len(visited):
            return True

    return len(boxes) == len(visited)

