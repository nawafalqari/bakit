'''
# BAKit
Built-in Alternative Kit

'''

from .Events import Event, Events
from .Queue import Queue
from .TasksQueue import TasksQueue
from .Copy import copy

__version__ = "1.0.1"
__all__ = ["Event", "Events", "Queue", "TasksQueue", "copy"]