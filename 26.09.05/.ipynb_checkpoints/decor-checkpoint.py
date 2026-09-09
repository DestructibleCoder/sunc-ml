import time

def functime(func):
    def wraper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()

        print(f'TIME: {(end - start):.5f}')
        return res
    return wraper