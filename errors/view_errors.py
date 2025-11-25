class ScreenNotFoundError(Exception):
    def __init__(self, screen):
        super().__init__(f"Screen '{screen}' was not found in view")

class ScreenMissingRequiredVariable(Exception):
    def __init__(self, screen, variable):
        super().__init__(f"Screen '{screen}' is missing the required variable '{variable}'")