from datetime import datetime
from time import time

def prettify_date(date, curr_date_format="%Y-%m-%d", new_date_format="%A %d %B, %Y"):
    """prettify_date(str, str) -> returns string of new date

    """
    date_time = datetime.strptime(str(date), curr_date_format)
    return datetime.strftime(date_time, new_date_format)


def date_now():
    """"""
    return datetime.utcnow()


def time_stamp():
    return str(time())

def get_time_passed_since(datetime_obj):

    time_now = datetime.utcnow()
    diff = time_now - datetime_obj
    days = diff.days
    mins, secs = divmod(diff.seconds, 60)

    time_passed = ""

    if days > 0:
        time_passed = "{}d ago".format(days)
    elif mins > 60:
        hours, seconds = divmod(mins, 60)
        time_passed = "{}h ago".format(hours)
    elif mins == 0 and secs > 0:
        time_passed = "{}s ago".format(secs)
    elif mins == 0 and secs == 0:
        time_passed = "just now"

    elif mins < 60:
        time_passed = "{}m {}s ago".format(mins, secs)
    return time_passed
