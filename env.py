import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".")/".env"
load_dotenv(dotenv_path=env_path)

API_URL=os.getenv("API_URL")
PHOTOS_API_URL=os.getenv("PHOTOS_API_URL")
LOGGER_PATH=os.getenv("LOGGER_PATH")
BARRIER_1_PORT=os.getenv("BARRIER_1_PORT")
BARRIER_2_PORT=os.getenv("BARRIER_2_PORT")
BAUDRATE=int(os.getenv("BAUDRATE"))
ID_BUILDING=int(os.getenv("ID_BUILDING"))
VERSION=os.getenv("VERSION")
