from datetime import datetime, timedelta


def time_mapper(time_interval):
    """Maps the time interval as given in the study to datetime.time.

    e.g. '001' -> datetime.time(4, 00)
    e.g. '144' -> datetime.time(3, 50)
    e.g. 1     -> datetime.time(4, 00)
    """
    time_interval = int(time_interval)
    if time_interval < 1 or time_interval > 144:
        raise ValueError('Invalid time invertal {}. Must be between 1 and 144.'
                         .format(time_interval))
    time_since_four = timedelta(minutes=(time_interval - 1) * 10)
    four = datetime(2000, 6, 10, 4, 0) # date does not matter
    time_step = four + time_since_four
    return time_step.time()
