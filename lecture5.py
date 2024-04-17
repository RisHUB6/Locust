# Sequential Task Set

from locust import SequentialTaskSet, HttpUser, task, constant

# Both of these task are run in a sequential order 
# first 200 status then 500
class MySequentialTask(SequentialTaskSet):
    
    @task
    def get_status(self):
        self.client.get("/200")
        print("Status 200")
    
    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Status 500")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MySequentialTask]
    weight_time = constant(1)