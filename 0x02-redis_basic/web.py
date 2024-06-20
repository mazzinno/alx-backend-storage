#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''Redis instance used for caching and tracking.
'''


def data_cacher(method: Callable) -> Callable:
    '''Decorator that caches the output of the decorated function.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''Wrapper function that handles caching and request tracking.
        '''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Fetches the content of a URL, caching the response and tracking the request count.
    '''
    return requests.get(url).text
