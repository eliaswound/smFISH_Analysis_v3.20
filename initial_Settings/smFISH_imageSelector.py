# image_selector.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox

class smFISH_ImageSelectorApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        self.setWindowTitle("Image Selector")
        self.layout = QVBoxLayout()

        # Initialize attributes to store selections
        self.useControlImage = False
        self.controlImagePath = None
        self.smFISHImagePath = None

        # Create toggle button for control image
        self.control_toggle_button = QPushButton("Enable Control Image")
        self.control_toggle_button.setCheckable(True)
        self.control_toggle_button.clicked.connect(self.toggle_control_button)
        self.layout.addWidget(self.control_toggle_button)

        # Create control image button, initially hidden
        self.control_image_button = QPushButton("Select Control Image")
        self.control_image_button.clicked.connect(self.select_control_image)
        self.control_image_button.setVisible(False)  # Start hidden
        self.layout.addWidget(self.control_image_button)

        # Create smFISH image button
        self.smfish_image_button = QPushButton("Select smFISH Image")
        self.smfish_image_button.clicked.connect(self.select_smfish_image)
        self.layout.addWidget(self.smfish_image_button)

        # Create finish button
        self.finish_button = QPushButton("Finish")
        self.finish_button.clicked.connect(self.finish)
        self.layout.addWidget(self.finish_button)

        # Set the layout
        self.setLayout(self.layout)

    def toggle_control_button(self):
        self.useControlImage = not self.useControlImage
        if self.useControlImage:
            self.control_toggle_button.setText("Disable Control Image")
            self.control_image_button.setVisible(True)
        else:
            self.control_toggle_button.setText("Enable Control Image")
            self.control_image_button.setVisible(False)
            self.controlImagePath = None  # Clear control image path if disabled

    def select_control_image(self):
        self.controlImagePath, _ = QFileDialog.getOpenFileName(self, "Please select your control Image")
        if self.controlImagePath:
            QMessageBox.information(self, "Selected File", f"Control Image selected: {self.controlImagePath}")

    def select_smfish_image(self):
        self.smFISHImagePath, _ = QFileDialog.getOpenFileName(self, "Please select your smFISH Image")
        if self.smFISHImagePath:
            QMessageBox.information(self, "Selected File", f"smFISH Image selected: {self.smFISHImagePath}")

    def finish(self):
        if (not self.useControlImage or self.controlImagePath) and self.smFISHImagePath:
            self.close()
        else:
            missing = []
            if self.useControlImage and not self.controlImagePath:
                missing.append("Control Image")
            if not self.smFISHImagePath:
                missing.append("smFISH Image")
            QMessageBox.warning(self, "Missing Files", f"Please select the following: {', '.join(missing)}")