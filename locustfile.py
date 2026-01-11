from locust import HttpUser, task, between

class CounterUser(HttpUser):
    wait_time = between(0.5, 2.0)

    @task(5)
    def root(self):
        self.client.get("/")

    @task(1)
    def health(self):
        self.client.get("/health")