import sys
import os
import collections
import shutil
import faulthandler
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image


ImageInfo = collections.namedtuple('ImageInfo', 'name, path, resolution')
wallpaper_resolutions = ['1280x800', '1440x900', '1680x1050', '1920x1200', '2560x1600', '1024x576', '1152x648', '1280x720', '1366x768', '1600x900', '1920x1080', '2560x1440', '3840x2160']


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        icon = os.path.join(os.getcwd(), 'preferences-desktop-wallpaper-symbolic.svg')
        self.setWindowIcon(QtGui.QIcon(icon))
        self.wallpaper_path = None
        self.full_file_path = None
        self.label_2_text = ''
        self.setObjectName('MainWindowObject')
        self.centralwidget = QtWidgets.QWidget(self)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setLineWidth(1)
        self.label.setText("<html><head/><body><pre style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"maincontent\"/><span style=\" font-family:\'SF Mono\';\"> _</span><span style=\" font-family:\'SF Mono\';\">_          __   _ _ _____                      _____         _______ </span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\';\"> \\ \\        / /  | | |  __ \\                    / ____|       |__   __|</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\';\">  \\ \\  /\\  / /_ _| | | |__) |_ _ _ __   ___ _ _| (___   ___  _ __| |   </span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\';\">   \\ \\/  \\/ / _` | | |  ___/ _` | \'_ \\ / _ \\ \'__\\___ \\ / _ \\| \'__| |   </span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\';\">    \\  /\\  / (_| | | | |  | (_| | |_) |  __/ |  ____) | (_) | |  | |   </span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\';\">     \\/  \\/ \\__,_|_|_|_|   \\__,_| .__/ \\___|_| |_____/ \\___/|_|  |_|   </span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\';\">                                | |                                    </span></pre><pre style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\';\">                                |_|                                    </span></pre><p><br/></p></body></html>")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(168, 0))
        self.progressBar.setProperty('value', 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.openDirectoryBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openDirectoryBtn.setObjectName("openDirectoryBtn")
        self.gridLayout.addWidget(self.openDirectoryBtn, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        spacer_item = QtWidgets.QSpacerItem(16, 16, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacer_item)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName("label_2")
        self.label_2.hide()
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        spacer_item1 = QtWidgets.QSpacerItem(16, 16, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacer_item1)
        self.SortButton = QtWidgets.QPushButton(self.centralwidget)
        self.SortButton.setObjectName("SortButton")
        self.horizontalLayout.addWidget(self.SortButton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslate_ui()
        self.openDirectoryBtn.clicked.connect(self.get_directory)
        self.SortButton.clicked.connect(self.sort)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.center_on_screen()
        self.show()

    def center_on_screen(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move(int((resolution.width() / 2) - (self.frameSize().width() / 2)), int((resolution.height() / 2) - (self.frameSize().height() / 2)))

    def get_directory(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory to Sort'))
        self.label_2_text = "Path Set: {}".format(file)
        self.label_2.show()
        self.retranslate_ui()
        self.full_file_path = os.path.abspath(file)

    def set_wallpaper_path(self):
        msgBox = QtWidgets.QMessageBox.question(self,'Set Output Path', "Default output path is: \n {} \n would you like to set custom?".format(self.wallpaper_path), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if msgBox == QtWidgets.QMessageBox.No:
            pass
        elif msgBox == QtWidgets.QMessageBox.Yes:
            file = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Wallpaper Sort Folder'))
            if os.path.isdir(file):
                self.wallpaper_path = os.path.abspath(file)
        else:
            pass

    def sort(self):
        search_subfolders = self.checkBox.isChecked()

        # sort subfolders and folders
        if self.full_file_path is not None:
            self.wallpaper_path = os.path.join(self.full_file_path, 'WallPaper_Sorted')
            self.SortButton.hide()
            self.checkBox.hide()
            self.openDirectoryBtn.hide()
            self.progressBar.show()
            self.set_wallpaper_path()
            self.label_2_text = "Beginning Sort..."
            self.retranslate_ui()
            QtCore.QCoreApplication.processEvents()

            try:
                os.mkdir(self.wallpaper_path)
            except FileExistsError:
                pass
            images = search_folder(self.full_file_path, search_subfolders)
            total_images = len(list(search_folder(self.full_file_path, search_subfolders)))
            total_image_count = 0
            image_count = 0
            for image in images:
                total_image_count += 1
                self.progressBar.setValue((total_image_count/total_images)*100)
                if image.resolution in wallpaper_resolutions:
                    new_path = os.path.join(self.wallpaper_path, image.resolution)
                    if not os.path.exists(new_path):
                        os.makedirs(new_path)
                        try:
                            shutil.copy(image.path, os.path.join(new_path, image.name))
                            image_count += 1
                        except shutil.SameFileError:
                            continue
                    else:
                        try:
                            shutil.copy(image.path, os.path.join(new_path, image.name))
                            image_count += 1
                        except shutil.SameFileError:
                            continue
                self.label_2_text = "{} out of {} Images Sorted".format(total_image_count, total_images)
                self.label_2.show()
                self.retranslate_ui()
                QtCore.QCoreApplication.processEvents()
            self.label_2.hide()
            if image_count > 0:
                self.label_2_text = '{} Images sorted to: {}'.format(image_count, self.wallpaper_path)
                self.label_2.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.label_2.show()
                self.retranslate_ui()
                QtCore.QCoreApplication.processEvents()
            else:
                self.label_2_text = "No Images Found"
                self.label_2.show()
                self.retranslate_ui()
                QtCore.QCoreApplication.processEvents()
            self.progressBar.hide()
            self.SortButton.show()
            self.checkBox.show()
            self.openDirectoryBtn.show()
        else:
            self.label_2_text = "No Directory Selected"
            self.label_2.show()
            self.retranslate_ui()
            QtCore.QCoreApplication.processEvents()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "WallPaperSorT"))
        self.openDirectoryBtn.setText(_translate("MainWindow", "Open Directory"))
        self.checkBox.setText(_translate("MainWindow", "Sort Subfolders?"))
        self.label_2.setText(_translate("MainWindow", self.label_2_text))
        self.SortButton.setToolTip(_translate("MainWindow", "Sorts pictures by resolution and copies them into a new directory"))
        self.SortButton.setText(_translate("MainWindow", "Sort"))


def search_image(filename):
    try:
        with Image.open(filename) as img:
            height, width = img.size
            resolution = str(height) + 'x' + str(width)
            images = ImageInfo(name=os.path.basename(filename), path=filename, resolution=resolution)
            yield images
    except(OSError, ValueError):
        return


def search_folder(folder, search_subfolders):
    items = os.listdir(folder)
    for item in items:
        full_path = os.path.join(folder, item)
        if os.path.isdir(full_path) and search_subfolders:
            yield from search_folder(full_path, search_subfolders)
        elif os.path.isdir(full_path) and not search_subfolders:
            continue
        else:
            yield from search_image(full_path)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())
