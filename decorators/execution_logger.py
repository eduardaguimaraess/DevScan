def execution_logger(func):

    def wrapper(self, response):

        print(f"[INFO] Running {self.name}...")

        result = func(self, response)

        print(f"[INFO] Finished {self.name}")

        return result

    return wrapper