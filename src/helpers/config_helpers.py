import os


def get_base_url():
    env = os.environ.get("test", "production")
    if env.lower() == "test":
        return "http://demostore.supersqa.com/"
