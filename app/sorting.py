from collections import Counter


def frequency_sort_string_counter(input_string: str):
    """
    >>> frequency_sort_string_counter('aabbbbbbccc')
    ['b', 'c', 'a']
    """
    counter = Counter(input_string)

    return list(char for char, freq in counter.most_common())

s = 'aabbbbbbccc'

c = Counter(s)
print(c)

print(Counter(s).most_common())


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

    #  From dictionary composing a list of, sorted by frequency
    sorted_frequency = sorted(frequency.items(), key=lambda value_to_sort: value_to_sort[1], reverse=True)
    result = []
    for (key, value) in sorted_frequency:
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


print(frequency_string_sort('aabbbbbbccc'))