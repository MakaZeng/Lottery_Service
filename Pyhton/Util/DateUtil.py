import time


def time_to_date(seconds):
    seconds = float(seconds)
    x = time.localtime(seconds)
    x = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return x