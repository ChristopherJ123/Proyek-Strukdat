from datetime import timedelta

class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.duration = timedelta()
        if hours == float('inf') or minutes == float('inf') or seconds == float('inf'):
            self.duration += timedelta(hours=9999)
        else:
            self.duration += timedelta(hours=hours, minutes=minutes, seconds=seconds)

    def __str__(self):
        total_seconds = int(self.duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def add_seconds(self, seconds):
        self.duration += timedelta(seconds=seconds)

    def add_minutes(self, minutes):
        self.duration += timedelta(minutes=minutes)

    def add_hours(self, hours):
        self.duration += timedelta(hours=hours)

    def get_time(self):
        total_seconds = int(self.duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return hours, minutes, seconds

    def get_time_formatted(self):
        total_seconds = int(self.duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def get_seconds(self):
        """Returns the total duration in seconds as a float."""
        return self.duration.total_seconds()

    def get_minutes(self):
        """Returns the total duration in minutes as a float."""
        return self.duration.total_seconds() / 60

    def get_hours(self):
        """Returns the total duration in hours as a float."""
        return self.duration.total_seconds() / 3600
