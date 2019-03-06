def frequency_sorting(elements: list):
    """
    Reduce the list to unique elements and sort them by frequency
    >>> frequency_sorting([1, 2, 1, 3, 3, 3, 3])
    [3, 1, 2]

    >>> frequency_sorting(['c', 'c', 'b', 'b', 'b', 'a'])
    ['b', 'c', 'a']
    """
    #  Composing a dictionary with 'elements': frequency pairs
    frequency = {}
    unique = set(elements)
    for u in unique:
        frequency[u] = elements.count(u)

    #  Composing a list, sorted by frequency
    result = []
    for x in range(len(frequency)):
        for key in frequency:
            if frequency[key] == max(frequency.values()) and max(frequency.values()) != 0:
                result.append(key)
                frequency[key] = 0
    return result


def frequency_string_sort(input_string):
    """
    >>> frequency_string_sort('aabbbbbbccc')
    'bbbbbbcccaa'
    """
    frequency = {}
    for character in input_string:
        frequency[character] = input_string.count(character)

    sorted_frequency = sorted(frequency.items(), key=lambda value_to_sort: value_to_sort[1], reverse=True)
    print(sorted_frequency)
    output = ''
    for k, v in sorted_frequency:
        for i in range(v):
            output += k
    return output
