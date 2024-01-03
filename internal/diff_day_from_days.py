import datetime


def return_day_calculate_diff_day_from_days(date_one):
    """
    Calculate diff day from days
    :param date_one:
    :return:
    """
    if date_one is None:
        return None
    date_one = datetime.datetime.strptime(str(date_one), "%Y-%m-%d %H:%M:%S")
    date_two = datetime.datetime.now()
    diff = date_two - date_one
    return diff.days


def return_age_calculate_diff_day_from_days(date_one):
    """
    Calculate diff day from days
    :param date_one:
    :return:
    """
    if date_one is None:
        return None
    date_one = datetime.datetime.strptime(str(date_one), "%Y-%m-%d %H:%M:%S")
    date_two = datetime.datetime.now()
    diff = date_two - date_one
    return diff.days / 365
