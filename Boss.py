from manager import QueueClient
import time
from Task import Task

class Boss(QueueClient):
    def __init__(self):
        super().__init__()

    
    def run(self):
        i = 1
        while True:
            tache = Task(i)
            self.tasks.put(tache)
            time.sleep(4)
            result = self.results.get()
            print("boss a récupéré resultat = " + str(result[0]) + " pour un temps de " + str(result[1]))
            
            i+=1


if __name__ == "__main__":
    b = Boss()
    b.run()