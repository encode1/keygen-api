"""
local.py is not found on production server
so this will raise an exception
"""
live = False
try:
    from .local import *
except:
    live = True

if live:
    from .production import *
