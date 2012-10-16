""" Settings for c300 """

from .base import *
try:
    from .local import *
except ImportError, exc:
    exc.args = tuple(
        ['%s (did you rename settings/local-temp.py?)' % exc.args[0]])
    raise exc
