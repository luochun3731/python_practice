def get_weekday(current_weekday, days_from_now):
    """
    (int, int) -> int

    Return which day of the week it will be days_from_now from current_weekday

    current_weekday is the current day of the week and is in the range 1-7, indicting
    whether today is Sunday (1), Monday (2), ..., Saturday (7)

    days_from_now is the number of days after today

    >>> get_weekday(3, 1)
    4
    >>> get_weekday(6, 1)
    7
    >>> get_weekday(7, 1)
    1
    >>> get_weekday(1, 0)
    1
    >>> get_weekday(4, 7)
    4
    >>> get_weekday(7, 72)
    2
    """

    return (current_weekday + days_from_now) % 7


if __name__ == '__main__':
    print(get_weekday(7, 72))
    print(get_weekday(4, 7))