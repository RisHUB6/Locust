import time
from locust import User, constant, task

class QuickstartUser(User):
    wait_time = constant(5)

    @task
    def hello_world(self):
        print("Printing the hello")

    @task
    def view_items(self):
        print("This is a view item")