import time
from locust import HttpUser, constant, task, wait_time, constant_pacing, between, User


class MyUser(User):
    
    # For constant waiting of 1 sec
    # wait_time = constant(1)
    
    # For a min and max waiting time
    # wait_time = between(4, 10)
    
    # This will check the execution time of task
    # If it finish before given time it will wait, it will take more than given time the next task execute 
    wait_time = constant_pacing(5)
    @task
    def launch(self):
        time.sleep(2)
        print("This will wait for 10 seconds delay")