class EnvironmentVariableNotFound(Exception):
    def __init__(self, variable):
        super().__init__(f"Environment variable '{variable}' was not found in loaded environment")