from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox,
    QMessageBox
)
from PyQt5.QtCore import pyqtSignal

class nucleiSegmentation_SettingsApp(QWidget):
    finished = pyqtSignal()  # Create a finished signal

    def __init__(self):
        super().__init__()

        # Set up the layout
        self.setWindowTitle("Nuclei Segmentation Settings")
        self.layout = QVBoxLayout()

        # Initialize parameters with default values
        self.nuclei_projection_size = 10  # Default value
        self.detection_thresh = [0.4, 0.3]  # Default values
        self.is_normalized = False
        self.normalize_thresh = [0.1, 99.0]  # Default values
        self.sample_percentage = 100  # Default value
        self.sample_region_size = [500, 500]  # Default values
        self.label_expansion_size = 20  # Default value

        # Input for Nuclei Projection Size
        self.layout.addWidget(QLabel("Nuclei Projection Size:"))
        self.nuclei_projection_input = QLineEdit(str(self.nuclei_projection_size))
        self.layout.addWidget(self.nuclei_projection_input)

        # Input for Detection Thresholds
        self.layout.addWidget(QLabel("Detection Threshold: Probabilty and Overlapping Thresh"))
        self.detection_min_input = QLineEdit(str(self.detection_thresh[0]))
        self.layout.addWidget(self.detection_min_input)
        self.detection_max_input = QLineEdit(str(self.detection_thresh[1]))
        self.layout.addWidget(self.detection_max_input)

        # Checkbox for Normalized Image
        self.normalized_checkbox = QCheckBox("Is Image Normalized Previously?")
        self.layout.addWidget(self.normalized_checkbox)

        # Input for Normalize Thresholds
        self.layout.addWidget(QLabel("Normalize Threshold (Min, Max):"))
        self.normalize_min_input = QLineEdit(str(self.normalize_thresh[0]))
        self.normalize_min_input.setEnabled(False)  # Initially disabled
        self.layout.addWidget(self.normalize_min_input)
        self.normalize_max_input = QLineEdit(str(self.normalize_thresh[1]))
        self.normalize_max_input.setEnabled(False)  # Initially disabled
        self.layout.addWidget(self.normalize_max_input)

        # Sample Percentage
        self.layout.addWidget(QLabel("Sample Percentage (0-100%):"))
        self.sample_percentage_input = QLineEdit(str(self.sample_percentage))
        self.layout.addWidget(self.sample_percentage_input)

        # Sample Region Size
        self.layout.addWidget(QLabel("Sample Region Size (Width, Height):"))
        self.sample_width_input = QLineEdit(str(self.sample_region_size[0]))
        self.layout.addWidget(self.sample_width_input)
        self.sample_height_input = QLineEdit(str(self.sample_region_size[1]))
        self.layout.addWidget(self.sample_height_input)

        # Label Expansion Size
        self.layout.addWidget(QLabel("Label Expansion Size:"))
        self.label_expansion_input = QLineEdit(str(self.label_expansion_size))
        self.layout.addWidget(self.label_expansion_input)

        # Save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_parameters)
        self.layout.addWidget(self.save_button)

        # Set the layout
        self.setLayout(self.layout)

        # Connect checkbox to enable/disable normalization inputs
        self.normalized_checkbox.stateChanged.connect(self.toggle_normalization_inputs)

    def toggle_normalization_inputs(self, state):
        # Enable or disable normalization input fields based on checkbox state
        is_checked = state == 2  # Checked state
        self.normalize_min_input.setEnabled(not is_checked)
        self.normalize_max_input.setEnabled(not is_checked)

    def save_parameters(self):
        # Retrieve inputs and validate them
        try:
            self.nuclei_projection_size = int(self.nuclei_projection_input.text())

            # Detection thresholds
            self.detection_thresh[0] = float(self.detection_min_input.text())
            self.detection_thresh[1] = float(self.detection_max_input.text())

            self.is_normalized = self.normalized_checkbox.isChecked()
            if not self.is_normalized:
                self.normalize_thresh[0] = float(self.normalize_min_input.text())
                self.normalize_thresh[1] = float(self.normalize_max_input.text())

                # Check that the second threshold is greater than the first
                if self.normalize_thresh[1] <= self.normalize_thresh[0]:
                    raise ValueError("Max threshold must be greater than Min threshold.")

            # Sample percentage
            self.sample_percentage = float(self.sample_percentage_input.text().strip('%'))

            # Sample region size
            self.sample_region_size[0] = int(self.sample_width_input.text())
            self.sample_region_size[1] = int(self.sample_height_input.text())

            # Label expansion size
            self.label_expansion_size = int(self.label_expansion_input.text())

            # Show saved parameters in a message box
            QMessageBox.information(self, "Parameters Saved",
                f"Nuclei Projection Size: {self.nuclei_projection_size}\n"
                f"Detection Threshold: {self.detection_thresh}\n"
                f"Is Image Normalized: {self.is_normalized}\n"
                f"Normalize Threshold: {self.normalize_thresh}\n"
                f"Sample Percentage: {self.sample_percentage}%\n"
                f"Sample Region Size: {self.sample_region_size}\n"
                f"Label Expansion Size: {self.label_expansion_size}"
            )
            self.finished.emit()  # Emit the finished signal
            self.close()  # Close the window after saving

        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))
