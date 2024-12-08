from datetime import timedelta

class Timer:
    def __init__(self):
        self.duration = timedelta()

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
        return f"{hours:02}:{minutes:02}:{seconds:02}"

# Example usage
timer = Timer()
timer.add_seconds(45)
timer.add_minutes(5)
timer.add_hours(1)

print("Timer duration:", timer.get_time(), "Ini dihapus dulu kalau mau di import")  # Outputs: Timer duration: 01:05:45
