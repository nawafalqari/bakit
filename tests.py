from time import sleep
from bakit.TasksQueue import TasksQueue

tq = TasksQueue(3)

def task(s=1):
   print(f"sleeping for {s}")
   sleep(s)
   print(f"finished {s}")

tq.execute(task)
tq.execute(task, 2)
tq.execute(task, 3)