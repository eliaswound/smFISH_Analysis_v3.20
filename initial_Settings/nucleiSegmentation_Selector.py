from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QCheckBox, QLabel, QFileDialog, QMessageBox
)
import sys


class nucleiSegmentation_SelectorApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        self.setWindowTitle("Nuclei Segmentation Parameters")
        self.layout = QVBoxLayout()

        # Initialize parameters
        self.perform_nuclei_segmentation = False
        self.nuclei_channel_path = None
        self.use_custom_model = False
        self.custom_model_directory = None

        # Checkbox for Perform Nuclei Segmentation
        self.segmentation_checkbox = QCheckBox("Perform Nuclei Segmentation")
        self.layout.addWidget(self.segmentation_checkbox)

        # Button for selecting Nuclei Channel Path
        self.nuclei_channel_button = QPushButton("Select Nuclei Channel File")
        self.nuclei_channel_button.setEnabled(False)  # Initially disabled
        self.nuclei_channel_button.clicked.connect(self.select_nuclei_channel)
        self.layout.addWidget(self.nuclei_channel_button)

        # Checkbox for Use Custom Model
        self.custom_model_checkbox = QCheckBox("Use Custom Model")
        self.layout.addWidget(self.custom_model_checkbox)

        # Button for selecting Custom Model Directory
        self.custom_model_button = QPushButton("Select Custom Model Directory")
        self.custom_model_button.setEnabled(False)  # Initially disabled
        self.custom_model_button.clicked.connect(self.select_custom_model_directory)
        self.layout.addWidget(self.custom_model_button)

        # Save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_parameters)
        self.layout.addWidget(self.save_button)

        # Set the layout
        self.setLayout(self.layout)

        # Connect checkboxes to enable buttons
        self.segmentation_checkbox.stateChanged.connect(self.toggle_nuclei_channel_button)
        self.custom_model_checkbox.stateChanged.connect(self.toggle_custom_model_button)

    def toggle_nuclei_channel_button(self, state):
        self.nuclei_channel_button.setEnabled(state == 2)  # Enable if checked

    def toggle_custom_model_button(self, state):
        self.custom_model_button.setEnabled(state == 2)  # Enable if checked

    def select_nuclei_channel(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Nuclei Channel File")
        if file_name:
            self.nuclei_channel_path = file_name

    def select_custom_model_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Custom Model Directory")
        if directory:
            self.custom_model_directory = directory

    def save_parameters(self):
        self.perform_nuclei_segmentation = self.segmentation_checkbox.isChecked()
        self.use_custom_model = self.custom_model_checkbox.isChecked()

        # Check if required selections were made
        if self.perform_nuclei_segmentation and not self.nuclei_channel_path:
            QMessageBox.warning(self, "Selection Error", "Please select a nuclei channel file.")
            return
        if self.use_custom_model and not self.custom_model_directory:
            QMessageBox.warning(self, "Selection Error", "Please select a custom model directory.")
            return

        # Display saved parameters
        QMessageBox.information(self, "Parameters Saved",
                                f"Perform Nuclei Segmentation: {self.perform_nuclei_segmentation}\n"
                                f"Nuclei Channel Path: {self.nuclei_channel_path}\n"
                                f"Use Custom Model: {self.use_custom_model}\n"
                                f"Custom Model Directory: {self.custom_model_directory}"
                                )
        self.close()  # Close the window after saving
