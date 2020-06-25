from PyQt5.QtWidgets import QProgressBar, QDialogButtonBox, QDialog, QInputDialog, QProgressBar, QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QListWidget, QListWidgetItem, QSlider
from PyQt5.QtCore import Qt


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.mainUI()
        self.setLayout()
        self.setWindowTitle("List App")
        self.setFixedSize(500, 300)
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

        # logic
        self.buttonAdd.clicked.connect(self.setInput)
        self.buttonRemove.clicked.connect(self.setRemove)
        self.buttonClear.clicked.connect(self.setClear)

        self.slider = QSlider(Qt.Horizontal)
        self.progressbar = QProgressBar()

    def setLayout(self):
        self.layoutList = QVBoxLayout()
        self.layoutList.addWidget(self.list)
        self.layoutList.addWidget(self.buttonAdd)
        self.layoutList.addWidget(self.buttonRemove)
        self.layoutList.addWidget(self.buttonUpdate)
        self.layoutList.addWidget(self.buttonClear)
        self.layoutList.addWidget(self.buttonDuplicate)
        self.layoutList.addWidget(self.slider)
        self.layoutList.addWidget(self.progressbar)

        self.setWidget = QWidget()
        self.setWidget.setLayout(self.layoutList)

    def setDialog(self):

        self.dialog = QDialog()
        self.dialog.setFixedSize(400, 200)
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

    # logic dialog

    def setInput(self):
        self.inputDialog, ok = QInputDialog.getText(
            self, "Add List App", "Enter Input")
        if ok == True:
            if self.inputDialog != "":
                self.add = QListWidgetItem(self.inputDialog, self.list)
                self.list.addItem(self.add)
                self.progressbar.setValue(self.list.count())
                print(f"check input dialog : {self.inputDialog}")
        print(ok)

    def setRemove(self):
        listdata_items = self.list.selectedItems()
        if not listdata_items:
            return
        for item in listdata_items:
            self.list.takeItem(self.list.row(item))
            self.progressbar.setValue(self.list.count())

    def setClear(self):
        self.list.clear()
        self.progressbar.setValue(self.list.count())

    def setUpdate(self):
        self.list.update()
        self.progressbar.setValue(self.list.count())


if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
