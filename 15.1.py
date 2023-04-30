import multiprocessing
import random
import time
from datetime import datetime

def worker():
    # Wait for a random number of seconds between 0 and 1
    time.sleep(random.random())
    # Print the current time
    print(f"Process {multiprocessing.current_process().name}: {datetime.now()}")
    # Exit the process
    multiprocessing.current_process().close()

if __name__ == '__main__':
    # Create three separate processes
    for i in range(3):
        p = multiprocessing.Process(target=worker, name=f"Process-{i}")
        p.start()
