from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QCheckBox, QPushButton, QFileDialog, QMessageBox
)

class counterstain_SelectionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Counterstain Image Selection")
        self.layout = QVBoxLayout()

        # Checkbox for selecting counterstain image
        self.counterstain_checkbox = QCheckBox("Do you want to select a counterstain image?")
        self.counterstain_checkbox.stateChanged.connect(self.toggle_selection_button)  # Connect state change to toggle function
        self.layout.addWidget(self.counterstain_checkbox)

        # Button to browse for counterstain image
        self.select_button = QPushButton("Select Counterstain Image")
        self.select_button.clicked.connect(self.select_counterstain_image)
        self.select_button.setEnabled(False)  # Initially disabled
        self.layout.addWidget(self.select_button)

        # Store the path of the counterstain image
        self.counterstain_image_path = None

        # Finish button to close the window
        self.finish_button = QPushButton("Finish")
        self.finish_button.clicked.connect(self.finish_selection)
        self.layout.addWidget(self.finish_button)

        # Set the layout
        self.setLayout(self.layout)

    def toggle_selection_button(self):
        # Enable or disable the select button based on the checkbox state
        self.select_button.setEnabled(self.counterstain_checkbox.isChecked())

    def select_counterstain_image(self):
        if self.counterstain_checkbox.isChecked():
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(self, "Select Counterstain Image")
            if file_path:
                self.counterstain_image_path = file_path
                QMessageBox.information(self, "Selected", f"Counterstain image selected:\n{file_path}")
            else:
                self.counterstain_image_path = None

    def finish_selection(self):
        if self.counterstain_checkbox.isChecked() and self.counterstain_image_path is None:
            QMessageBox.warning(self, "Selection Error", "Please select a counterstain image before finishing.")
        else:
            # Show the selected counterstain image path in a message box
            if self.counterstain_checkbox.isChecked():
                QMessageBox.information(self, "Counterstain Image Selected", f"Counterstain image path:\n{self.counterstain_image_path}")
            else:
                QMessageBox.information(self, "No Selection", "No counterstain image selected.")
            self.close()