class OutOfScheduleError(Exception):
    def __init__(self, message=None):
        self.message = message or "Transaction is out of schedule"
