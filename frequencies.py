"""Frequencies function."""

"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequency_dict = {}
    # Your code goes here
    for item in items:
        key: str = item if isinstance(item, str) else str(item)

        if key not in frequency_dict:
            frequency_dict[key] = 0

        frequency_dict[key] += 1

    return frequency_dict
