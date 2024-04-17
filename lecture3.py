from locust import TaskSet, constant, task, HttpUser

class MyHTTPClass(TaskSet): # we cannot directly starts the TaskSet we need a User class
    
    @task
    def get_status(self):
        self.client.get("/200")
        print("Status of 200")


class MyLoadTesting(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPClass]
    wait_time = constant(1)