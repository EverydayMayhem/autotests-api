import time

def get_random_email() ->str:
    return f'user.{time.time()}@example.com'