from PyQt5.QtWidgets import QProgressBar, QDialogButtonBox, QDialog, QInputDialog, QProgressBar, QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QListWidget, QListWidgetItem, QSlider
from PyQt5.QtCore import Qt


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.mainUI()
        self.setLayout()
        self.setWindowTitle("List App")
        self.setFixedSize(400, 300)
        self.setCentralWidget(self.setWidget)

    def mainUI(self):
        self.list = QListWidget()
        self.buttonAdd = QPushButton("Add")
        self.buttonRemove = QPushButton("Remove")
        self.buttonUpdate = QPushButton("update")
        self.buttonClear = QPushButton("clear all")
        self.buttonDuplicate = QPushButton("duplicate")
        # self.buttonDialog = QPushButton("Open Dialog Box")
        # self.buttonInputDialog = QPushButton("Open Input Dialog")
        # self.buttonDialog.clicked.connect(self.setDialog)
        self.buttonAdd.clicked.connect(self.setInputDialog)
        self.slider = QSlider()
        self.Progressbar = QProgressBar()
        self.Progressbar.setValue(30)

    def setLayout(self):
        self.layoutList = QVBoxLayout()
        self.layoutList.addWidget(self.list)
        self.layoutList.addWidget(self.buttonAdd)
        self.layoutList.addWidget(self.buttonRemove)
        self.layoutList.addWidget(self.buttonUpdate)
        self.layoutList.addWidget(self.buttonClear)
        self.layoutList.addWidget(self.buttonDuplicate)
        self.layoutList.addWidget(self.slider)
        self.layoutList.addWidget(self.Progressbar)

        self.setWidget = QWidget()
        self.setWidget.setLayout(self.layoutList)

    def setDialog(self):

        self.dialog = QDialog()
        self.dialog.setFixedSize(300, 200)
        self.dialog.setWindowTitle("Custom Dialog Box")

        self.labelDialog = QLabel("custom label")
        self.button = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(self.button)
        self.buttonBox.accepted.connect(self.dialog.accept)

        self.layoutDialog = QVBoxLayout()
        self.layoutDialog.addWidget(self.labelDialog)
        self.layoutDialog.addWidget(self.buttonBox)

        self.dialog.setLayout(self.layoutDialog)
        self.dialog.exec_()

    def setInputDialog(self):
        self.inputDialog, ok = QInputDialog.getText(
            self, "Add New List", "add list item")
        print(f"cek input dialog : {self.inputDialog}")
        print(ok)

    # def setRemoveDialog(self):
    #     self.removeDialog, ok = QIn


if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
