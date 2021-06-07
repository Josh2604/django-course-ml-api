import time
from locust import HttpUser, task, between

# DOC: https://docs.locust.io/en/stable/quickstart.html#example-locustfile-py


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(1)
    def get_all(self):
        self.client.get("/api/v1/users/all")