import functools


def now():
    print('2015-3-25')


now()
f = now
f()

print(now.__name__)
print(f.__name__)


################################################################################

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


log(now)()

now()


@log
def now():
    print('2015-3-25')


now()


################################################################################

def now():
    print('2015-3-25')


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


log('execute')(now)()


@log('execute')
def now():
    print('2015-3-25')


now()
print(now.__name__)


################################################################################

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()
print(now.__name__)


################################################################################

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()
print(now.__name__)
