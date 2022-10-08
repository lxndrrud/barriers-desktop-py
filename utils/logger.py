from datetime import datetime
from env import LOGGER_PATH

class Logger:
    def writeToLogs(self, toWrite: str):
        with open(LOGGER_PATH + 'log.txt', 'a') as file_:
            print(file_.write(f"[{datetime.now()}]: " + toWrite + "\n"))
