import time


def time_to_date(seconds):
    seconds = float(seconds)
    x = time.localtime(seconds)
    x = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return x

def date_to_time(str):
    x = time.strptime(str, '%Y-%m-%d %H:%M:%S')
    x = time.mktime(x)
    return x