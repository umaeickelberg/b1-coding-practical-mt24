class PDController:
    def __init__(self):
        self.previous_error = 0.0

    def __call__(self, observation, reference):
        error = reference - observation
        action = 0.15 * error + 0.6 * (error - self.previous_error)
        self.previous_error = error
        return action

    def reset(self):
        self.previous_error = 0.0