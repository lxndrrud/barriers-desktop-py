from PySide6.QtWidgets import QWidget
import widgets.personal_movement_modal.ui_personal_movement_modal


class PersonalMovementModal(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui_form = widgets.personal_movement_modal.ui_personal_movement_modal.Ui_Form()
        self.ui_form.setupUi(self)

    def setup(self):
        pass



