class UserNotFoundException(Exception):
    def __init__(self):
        self.message = "User not found"

class TaskNotFoundException(Exception):
    def __init__(self):
        self.message = "Task not found"