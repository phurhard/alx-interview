#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Returns True or false if all the boxes passed to it can be unlocked

    Keyword arguments:
    boxes -- A list of list of boxes with keys
    Return: Returns true or false
    """

    n = len(boxes)
    keysToCheck = set()

    unlockedBoxes = {0}
    keysToCheck.update(boxes[0])

    while keysToCheck:
        key = keysToCheck.pop()
        if key < 0 or key >= n:
            continue

        if key not in unlockedBoxes:
            unlockedBoxes.add(key)
            keysToCheck.update(boxes[key])

    return len(unlockedBoxes) == n
