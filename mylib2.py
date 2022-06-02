def myfunc():
    print("in myfunc()")


def echo(event):
    print(event)
    return event


def double(event):
    return event * 2


def add3(event):
    return event + 3

from mlrun.runtimes import nuclio_init_hook
def init_context(context):
    nuclio_init_hook(context, globals(), 'serving_v2')

def handler(context, event):
    return context.mlrun_handler(context, event)
