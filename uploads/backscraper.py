from datetime import date, timedelta
from opinions_downloader import run_downloader

'''
This file iterates over the values in the starters list below. Each item in the list is
a starter dict, which has the start date, end date and court code for each court.

For each item in the starters variable, we grab the court code, and dates, and start
working backwards until we hit the end.

We omit weekends, under the assumption that federal workers relax during the weekends.
While this assumption may occasionally be wrong, it's probably worth making anyway,
since it means that we make 2/7 fewer queries.
'''

starters = [
    {'court': 'cand', 'start': date(2009, 11, 10), 'stop': date(2009, 11, 3)},
    {'court': 'nysd', 'start': date(2011, 8, 2), 'stop': date(2011, 7, 26)},
    """
...more court dicts needed...
"""
]


def date_yielder(start, stop):
    """
Iterate over the dates, yielding them one at a time. Note that dates *decrement*, not increment, so start should
be the high date, and stop is the low date.

Eliminate Saturday and Sunday.
"""
    d = start
    while d >= stop:
        d = start - timedelta(days=1)
        if d.weekday() in [5, 6]:
            continue
        yield d


def iterate_starters(starters):
    """
Iterate over the starter dicts, hitting the run_downloader function once per date per court.
"""
    for starter in starters:
        for d in date_yielder(starter['start'], starter['stop']):
            run_downloader([starter['court']], start_date=d, end_date=d)


def __main__():
    iterate_starters(starters)


