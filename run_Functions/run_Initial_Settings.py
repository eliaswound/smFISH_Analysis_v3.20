from PyQt5.QtWidgets import QApplication
from initial_Settings.smFISH_imageSelector import smFISH_ImageSelectorApp
from initial_Settings.smFISH_parameters import smFISH_ParametersApp
from initial_Settings.smFISH_spotPlotSettings import smFISH_spotPlotSettingsApp
from initial_Settings.nucleiSegmentation_Selector import nucleiSegmentation_SelectorApp
from initial_Settings.nucleiSegmentation_Settings import nucleiSegmentation_SettingsApp
from initial_Settings.counterstain_ImageSelector import counterstain_SelectionApp
import sys

def run_init_settings():
    app = QApplication(sys.argv)

    # Run the Image Selector
    selector = smFISH_ImageSelectorApp()
    selector.show()
    app.exec_()

    # Run the SMFISH Parameters input
    smfish_parameters = smFISH_ParametersApp()
    smfish_parameters.show()
    app.exec_()

    # Run the Spot Parameters input
    spot_parameters = smFISH_spotPlotSettingsApp()
    spot_parameters.show()
    app.exec_()

    # Run the Nuclei Segmentation input
    nuclei_segmentation = nucleiSegmentation_SelectorApp()
    nuclei_segmentation.show()
    app.exec_()
    if nuclei_segmentation.perform_nuclei_segmentation:
        nuclei_segmentation_settings = nucleiSegmentation_SettingsApp()
        nuclei_segmentation_settings.show()
        app.exec_()

    counterstain_selection = counterstain_SelectionApp()
    counterstain_selection.show()
    app.exec_()

    # Exit the application after closing the last window
    sys.exit()
