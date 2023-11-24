from manager import QueueClient
import time
import Task

class Minion(QueueClient):
    def __init__(self):
        super().__init__()

    
    def run(self):
        while True:
            time.sleep(1)
            task, i = self.tasks.get()
            result = task.work()
            self.results.put((task.x, task.time, i))

if __name__ == "__main__":
    m = Minion()
    m.run()