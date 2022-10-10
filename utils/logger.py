from datetime import datetime
import os
from env import LOGGER_PATH

class Logger:
    def __init__(self) -> None:
        if not os.path.exists(LOGGER_PATH):
            os.makedirs(LOGGER_PATH)

    def writeToLogs(self, toWrite: str):
        with open(LOGGER_PATH + 'log.txt', 'a') as file_:
            print(file_.write(f"[{datetime.now()}]: " + toWrite + "\n"))
