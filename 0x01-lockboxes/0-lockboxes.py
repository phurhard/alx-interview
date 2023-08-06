#!/usr/bin/env python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Returns True or false if all the boxes passed to it can be unlocked

    Keyword arguments:
    boxes -- A list of list of boxes with keys
    Return: Returns true or false
    """
    unlockedBoxes = []
    unlockedBoxes.append(boxes[0])
    keysToCheck = []
    keysToCheck = boxes[0]
    n = len(boxes)

    for key in keysToCheck:
        # print(f'Unlocked boxes before the next iteration {unlockedBoxes}')
        if boxes[key] in unlockedBoxes:
            # print(f'Boxes[key] === {boxes[key]}')

            continue
    #         # print(boxes[key])
        else:
            unlockedBoxes.append(boxes[key])
            # print(f'unlockedBoxes == {unlockedBoxes}')
            keysToCheck += boxes[key]
            # print(f'keysTocheck == {keysToCheck}')
    if len(unlockedBoxes) == len(boxes):
        return True
    else:
        return False
