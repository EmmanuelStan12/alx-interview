#!/usr/bin/python3
"""Calculates if all boxes in a given set can be opened"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    """
    queue = [0]
    visited = {0}
    return traverse(boxes, queue, visited)


def traverse(boxes, queue, visited):
    """
    Traverse the boxes using keys and a queue
    """
    while queue:
        index = queue.pop(0)
        if index not in visited:
            visited.add(index)

        for key in boxes[index]:
            if key not in visited and 0 <= key < len(boxes):
                queue.append(key)

        if len(boxes) == len(visited):
            return True

    return len(boxes) == len(visited)
