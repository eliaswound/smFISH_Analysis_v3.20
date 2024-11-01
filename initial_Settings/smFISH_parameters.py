from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)

class smFISH_ParametersApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        self.setWindowTitle("Time to input smFISH Parameters")
        self.layout = QVBoxLayout()

        # Initialize default parameters
        self.minimal_distance = [2, 2, 2]
        self.kernel_size = [1, 1.5, 1.5]
        self.voxel_size = [361, 75, 75]
        self.spot_size = [600, 300, 300]
        self.decomposition_thresh = [0.7, 1, 5]

        # Input fields for Minimal Distance
        self.minimal_distance_inputs = []
        self.layout.addWidget(QLabel("Please enter Minimal Distance in integer pixel (z, y, x):"))
        min_dist_layout = QHBoxLayout()
        for i, default_value in enumerate(self.minimal_distance):
            line_edit = QLineEdit(str(default_value))
            min_dist_layout.addWidget(line_edit)
            self.minimal_distance_inputs.append(line_edit)
        self.layout.addLayout(min_dist_layout)

        # Input fields for Kernel Size
        self.kernel_size_inputs = []
        self.layout.addWidget(QLabel("Please enter Gaussian filter Kernel Size (z, y, x):"))
        kernel_size_layout = QHBoxLayout()
        for i, default_value in enumerate(self.kernel_size):
            line_edit = QLineEdit(str(default_value))
            kernel_size_layout.addWidget(line_edit)
            self.kernel_size_inputs.append(line_edit)
        self.layout.addLayout(kernel_size_layout)

        # Input fields for Voxel Size
        self.voxel_size_inputs = []
        self.layout.addWidget(QLabel("Please Enter Integer Voxel Size in um (z, y, x):"))
        voxel_size_layout = QHBoxLayout()
        for i, default_value in enumerate(self.voxel_size):
            line_edit = QLineEdit(str(default_value))
            voxel_size_layout.addWidget(line_edit)
            self.voxel_size_inputs.append(line_edit)
        self.layout.addLayout(voxel_size_layout)

        # Input fields for Spot Size
        self.spot_size_inputs = []
        self.layout.addWidget(QLabel("Please Enter Integer Spot Size in um (z, y, x):"))
        spot_size_layout = QHBoxLayout()
        for i, default_value in enumerate(self.spot_size):
            line_edit = QLineEdit(str(default_value))
            spot_size_layout.addWidget(line_edit)
            self.spot_size_inputs.append(line_edit)
        self.layout.addLayout(spot_size_layout)

        # Input fields for Spot Size
        self.decomposition_thresh_inputs = []
        self.layout.addWidget(QLabel("Please enter Decomposition Threshold (alpha, beta, gamma):"))
        decomposition_thresh_layout = QHBoxLayout()
        for i, default_value in enumerate(self.decomposition_thresh):
            line_edit = QLineEdit(str(default_value))
            decomposition_thresh_layout.addWidget(line_edit)
            self.decomposition_thresh_inputs.append(line_edit)
        self.layout.addLayout(decomposition_thresh_layout)

        # Create Save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_parameters)
        self.layout.addWidget(self.save_button)

        # Set the layout
        self.setLayout(self.layout)

    def save_parameters(self):
        # Save Minimal Distance values
        try:
            self.minimal_distance = [
                int(self.minimal_distance_inputs[0].text()),
                int(self.minimal_distance_inputs[1].text()),
                int(self.minimal_distance_inputs[2].text())
            ]
            # Save Kernel Size values
            self.kernel_size = [
                float(self.kernel_size_inputs[0].text()),
                float(self.kernel_size_inputs[1].text()),
                float(self.kernel_size_inputs[2].text())
            ]
            # Save Voxel Size values
            self.voxel_size = [
                int(self.voxel_size_inputs[0].text()),
                int(self.voxel_size_inputs[1].text()),
                int(self.voxel_size_inputs[2].text())
            ]
            # Save Spot Size values
            self.spot_size = [
                int(self.spot_size_inputs[0].text()),
                int(self.spot_size_inputs[1].text()),
                int(self.spot_size_inputs[2].text())
            ]

            self.decomposition_thresh = [
                float(self.decomposition_thresh_inputs[0].text()),
                float(self.decomposition_thresh_inputs[1].text()),
                float(self.decomposition_thresh_inputs[2].text())
            ]
            QMessageBox.information(self, "Parameters Saved",
                                    f"Minimal Distance: {self.minimal_distance}\n"
                                    f"Kernel Size: {self.kernel_size}\n"
                                    f"Voxel Size: {self.voxel_size}\n"
                                    f"Spot Size: {self.spot_size}\n"
                                    f"Decomposition Thresh: {self.decomposition_thresh}\n"
                                    )
            self.close()  # Close the window after saving

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values for all parameters.")


