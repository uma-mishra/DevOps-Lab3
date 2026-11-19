from locust import HttpUser, task, between


class FeatureFlagUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def open_dashboard(self):
        self.client.get("/")

    @task(2)
    def get_feature_flags(self):
        self.client.get("/api/flags")

    @task(1)
    def check_flag(self):
        self.client.post("/api/flags/dark_mode/on")
