from locust import HttpUser, constant, task


class MyReqRes(HttpUser):
    host = "https://regres.in"
    wait_time = constant(1)
    
    @task
    def get_user(self):
        res = self.client.get("/api/users?page=2")
        print(res.text)
    
    @task
    def create_user(self):
        res = self.client.post("/api/users", data = """
                                                    {"name":"Rishabh", 
                                                    "job":"Leader"}""")
        print(res.text)