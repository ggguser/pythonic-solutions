from collections import Counter


def frequency_sort_string_counter(input_string: str):
    """
    >>> frequency_sort_string_counter('aabbbbbbccc')
    ['b', 'c', 'a']
    """
    counter = Counter(input_string)

    return list(char for char, freq in counter.most_common())


def frequency_sorting_manual(elements: list):
    """
    Reduce the list to unique elements and sort them by frequency
    >>> frequency_sorting_manual([1, 2, 1, 3, 3, 3, 3])
    [3, 1, 2]

    >>> frequency_sorting_manual(['c', 'c', 'b', 'b', 'b', 'a'])
    ['b', 'c', 'a']

    >>> frequency_sorting_manual([3, 3, 1, 2, 1, 2])
    [1, 2, 3]
    """
    #  Composing a dictionary with 'elements': frequency pairs
    frequency = {}
    unique = set(elements)
    for u in unique:
        frequency[u] = elements.count(u)

    #  From dictionary composing a list of, sorted by frequency
    result = []
    for x in range(len(frequency)):
        for key in frequency:
            if frequency[key] == max(frequency.values()) and max(frequency.values()) != 0:
                result.append(key)
                frequency[key] = 0
    return result


def frequency_list_sorting_simplified(elements: list):
    """
    Reduce the list to unique elements and sort them by frequency
    >>> frequency_list_sorting_simplified([1, 2, 1, 3, 3, 3, 3])
    [3, 1, 2]

    >>> frequency_list_sorting_simplified([1, 2, 1, 2, 3, 3])
    [1, 2, 3]

    >>> frequency_list_sorting_simplified(['c', 'c', 'b', 'b', 'b', 'a'])
    ['b', 'c', 'a']
    """
    #  Composing a dictionary with 'elements': frequency pairs
    frequency = Counter(elements)
    #  From dictionary composing a list of tuples, sorted by frequency
    sorted_frequency = frequency.most_common()
    #  From that list getting only the keys
    result = []
    for key, value in sorted_frequency:
        result.append(key)
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
    output = ''
    for k, v in sorted_frequency:
        for i in range(v):
            output += k
    return output
