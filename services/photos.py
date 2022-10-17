from env import PHOTOS_API_URL
from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QPixmap
import requests

class PhotosService(QObject):
    showException = Signal(str)

    def __init__(self) -> None:
        super().__init__()

    def get_photo(self, photo_path: str):
        try:
            response = requests.get(f"{PHOTOS_API_URL}/{photo_path}")
            if response.status_code != 200:
                raise Exception(f"ошибка сервера -> {response.json()}")
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            return pixmap
        except Exception as e:
            self.showException.emit(f"Ошибка во время получения фото: {e}")
            return None
