def comma_separator(number) -> str:
    """
    >>> comma_separator(1000000)
    '1,000,000'
    """
    return f"{number:,}"


def space_separator(number) -> str:
    """
    >>> space_separator(1000000)
    '1 000 000'
    """
    return f"{number:_}".replace('_', ' ')
