class ScreenNotFoundError(Exception):
    def __init__(self, screen):
        super().__init__(f"Screen '{screen}' was not found in view")