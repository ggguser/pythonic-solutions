from datetime import datetime, timezone, timedelta


def get_time_diff(time_in_iso):
    """
    Converts 2020-05-09T01:16:22.893Z to 2020-05-09 01:16
    Converts 2020-05-09T01:16:22.8Z to 2020-05-09 01:16
    Converts 2020-05-09T01:16:22Z to 2020-05-09 01:16
    """
    # assert is_iso_date(time_in_iso)
    time_pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
    if '.' not in time_in_iso:
        time_pattern = '%Y-%m-%dT%H:%M:%SZ'
    future = datetime.strptime(time_in_iso, time_pattern)
    now = datetime.now(timezone.utc).replace(microsecond=0, tzinfo=None)
    diff = future - now
    return diff.total_seconds()


def get_date_from_now(seconds=0, *, minutes=0, hours=0, days=0):
    """
    Creates a string with date in '2020-05-09T01:16:22Z' format

    :param seconds: int or float
    :param minutes: int
    :param hours: int
    :param days: int
    :return: str
    """
    today = datetime.now(timezone.utc).replace(microsecond=0, tzinfo=None)
    new_date = today + timedelta(seconds=seconds, minutes=minutes, hours=hours, days=days)
    iso_new_date = new_date.isoformat(timespec='milliseconds')
    _, microseconds = iso_new_date.split('.')
    index = 0
    for i in range(len(microseconds)):
        if microseconds.endswith('0' * i):
            index = i
    milliseconds = int(microseconds[:-index])
    milliseconds = f'.{milliseconds}' if milliseconds else ''
    return new_date.isoformat(timespec='seconds') + milliseconds + 'Z'


def is_iso_date(date_in_iso):
    """Checks whether the given date matches the Cinarra format"""
    time_pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
    if '.' not in date_in_iso:
        time_pattern = '%Y-%m-%dT%H:%M:%SZ'
    try:
        datetime.strptime(date_in_iso, time_pattern)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    future = get_date_from_now(10000.00001)
    print(future)


