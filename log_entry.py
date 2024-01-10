import datetime

class LogEntry:
    def __init__(self, id_str, date_time) -> None:
        self.id_str = id_str
        self.date = datetime.datetime(date_time)
        
