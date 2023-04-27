from locust import HttpUser, between, task
import time


start_time = time.time()

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def list_of_blogs(self):
        for i in range(10):
            self.client.get("/blogs/list")

    # @task
    # def create_blog_post(self):
    #     # for j in range(10):
    #         self.client.post(
    #             "/blogs/create", 
    #             json={
    #                 "user_id": 1,
    #                 "title": "Mock Title", 
    #                 "content": "asdfasfajglrjgwerhjasdfasdfasdfasdfasdfasdf",
    #                 "image": "profile.png"
    #             }
    #         )

    # @task
    # def register(self):
    #     # for k in range(10):
    #         self.client.post(
    #             "/accounts/register", 
    #             json={
    #                 "username": "Mock User", 
    #                 "email": "mock@gmail.com", 
    #                 "password": "20051205",
    #                 "gender": "Male",
    #                 "birthdate": "02/01/2005",
    #                 "bio": "Mock BIOasdasdasdasdasd"
    #             }
    #         )

end_time = time.time()
print(end_time-start_time)
