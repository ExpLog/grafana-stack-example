from functools import wraps

from prometheus_client import Histogram

# this histogram is using the default registry for prometheus
REQUEST_TIME = Histogram("req_time_seconds", "time spent in HTTP requests", ('method', 'path'))


# the sync context managers work fine
def async_time(histogram: Histogram, *label_values: str, **label_kwargs: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            with histogram.labels(*label_values, **label_kwargs).time():
                return await func(*args, **kwargs)

        return wrapper

    return decorator

