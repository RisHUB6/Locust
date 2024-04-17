# Here we learn about nested task set and two class task set
from locust import TaskSet, HttpUser, constant, task


# This is the nested task set
# uncomment the code from line 7 to line 23 
# class MyHTTPClass(TaskSet): # we cannot directly starts the TaskSet we need a User class
    
#     @task
#     def get_status(self):
#         self.client.get("/200")
#         print("Status of 200")
    
#     @task
#     class MyAnotherHTTPCat(TaskSet):
        
#         @task
#         def get_500_status(self):
#             self.client.get("/500")
#             print("Getting 500") # At this stage code will stuck in it
#             # so we have to use
#             # self.interrupt() # But this will bring it one by one
#             self.interrupt(reschedule=False) # we will reschedule this.
            


# Now we are having the different class of task set
class MyHTTPClass(TaskSet): # we cannot directly starts the TaskSet we need a User class
    
    @task
    def get_status(self):
        self.client.get("/200")
        print("Status of 200")
        self.interrupt(reschedule=False) # By adding the interrupt it will leave this class
    
class MyAnotherHTTPCat(TaskSet):
    
    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Getting 500")
        self.interrupt(reschedule=False)


class MyLoadTesting(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPClass, MyAnotherHTTPCat]
    wait_time = constant(1)