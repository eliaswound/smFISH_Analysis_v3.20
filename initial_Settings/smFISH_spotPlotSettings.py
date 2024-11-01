from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QCheckBox, QMessageBox
)

class smFISH_spotPlotSettingsApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        self.setWindowTitle("Spot Plot Settings")
        self.layout = QVBoxLayout()

        # Initialize default parameters
        self.spots_radius_detection = True
        self.plot_spot_size = 4
        self.plot_inner_circle = False
        self.exact_plot_size = 2
        self.save_spot_information = True
        self.plot_spot_label = False

        # Checkbox for Spots Radius Detection
        self.spots_radius_checkbox = QCheckBox("Enable Spots Radius Detection")
        self.spots_radius_checkbox.setChecked(self.spots_radius_detection)
        self.spots_radius_checkbox.stateChanged.connect(self.toggle_plot_spot_size)
        self.layout.addWidget(self.spots_radius_checkbox)

        # Input for Plot Spot Size
        self.plot_spot_size_input = QLineEdit(str(self.plot_spot_size))
        self.plot_spot_size_input.setEnabled(self.spots_radius_detection)
        self.layout.addWidget(QLabel("Plotted Spot Size in Pixel size (integer):"))
        self.layout.addWidget(self.plot_spot_size_input)

        # Checkbox for Plot Inner Circle
        self.plot_inner_circle_checkbox = QCheckBox("Enable Plot Inner Circle (beta Testing Function)")
        self.plot_inner_circle_checkbox.setChecked(self.plot_inner_circle)
        self.plot_inner_circle_checkbox.stateChanged.connect(self.toggle_exact_plot_size)
        self.layout.addWidget(self.plot_inner_circle_checkbox)

        # Input for Exact Plot Size
        self.exact_plot_size_input = QLineEdit(str(self.exact_plot_size))
        self.exact_plot_size_input.setEnabled(self.plot_inner_circle)
        self.layout.addWidget(QLabel("Exact Plot Size in Pixel (integer):"))
        self.layout.addWidget(self.exact_plot_size_input)

        # Checkbox for Save Spot Information
        self.save_spot_info_checkbox = QCheckBox("Save Spot Information")
        self.save_spot_info_checkbox.setChecked(self.save_spot_information)
        self.layout.addWidget(self.save_spot_info_checkbox)

        # Checkbox for Plot Spot Label
        self.plot_spot_label_checkbox = QCheckBox("Plot Spot Label")
        self.plot_spot_label_checkbox.setChecked(self.plot_spot_label)
        self.layout.addWidget(self.plot_spot_label_checkbox)

        # Create Save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_parameters)
        self.layout.addWidget(self.save_button)

        # Set the layout
        self.setLayout(self.layout)

    def toggle_plot_spot_size(self, state):
        self.plot_spot_size_input.setEnabled(state == 2)  # Enable if checked

    def toggle_exact_plot_size(self, state):
        self.exact_plot_size_input.setEnabled(state == 2)  # Enable if checked

    def save_parameters(self):
        # Save parameters
        try:
            self.spots_radius_detection = self.spots_radius_checkbox.isChecked()
            self.plot_spot_size = int(self.plot_spot_size_input.text())
            self.plot_inner_circle = self.plot_inner_circle_checkbox.isChecked()
            self.exact_plot_size = int(self.exact_plot_size_input.text()) if self.plot_inner_circle else None
            self.save_spot_information = self.save_spot_info_checkbox.isChecked()
            self.plot_spot_label = self.plot_spot_label_checkbox.isChecked()

            QMessageBox.information(self, "Parameters Saved",
                f"Spots Radius Detection: {self.spots_radius_detection}\n"
                f"Plot Spot Size: {self.plot_spot_size}\n"
                f"Plot Inner Circle: {self.plot_inner_circle}\n"
                f"Exact Plot Size: {self.exact_plot_size}\n"
                f"Save Spot Information: {self.save_spot_information}\n"
                f"Plot Spot Label: {self.plot_spot_label}"
            )
            self.close()  # Close the window after saving

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values for plot sizes.")

