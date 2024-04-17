# Validate the response of the api call

from locust import HttpUser, task, constant, SequentialTaskSet


class MyScript(HttpUser):
    
    @task
    def get_xml(self):
        result = self