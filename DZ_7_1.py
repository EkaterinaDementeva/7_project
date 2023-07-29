from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds


class MyCustomWidget(QtWidgets.QDialog):
    def __init__(self):
        super(MyCustomWidget, self).__init__()
        self.selected_objects = []
        self.widgets = []  # список созданных виджетов
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("My Custom UI")
        self.setObjectName("MyCustomWidgetUIId")
        self.setMinimumSize(300, 500)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.main_layout)

        # кнопка добавления нового виджета
        self.btn_add = QtWidgets.QPushButton("+")
        self.btn_add.clicked.connect(self.add_widget)
        self.main_layout.addWidget(self.btn_add)

    def add_widget(self):
        self.get_selection()
        widget = CustomButtonWidget(self.selected_objects)
        self.widgets.append(widget)
        self.main_layout.addWidget(widget)

    def get_selection(self):
        self.selected_objects = cmds.ls(sl=True, long=True)


class CustomButtonWidget(QtWidgets.QWidget):
    def __init__(self, selected_objects):
        super(CustomButtonWidget, self).__init__()

        self.selected_objects = selected_objects

        layout = QtWidgets.QHBoxLayout()

        self.label = QtWidgets.QLabel()
        self.label.setText("Selected objects: {}".format(self.selected_objects))
        layout.addWidget(self.label)

        self.btn = QtWidgets.QPushButton("Select")
        layout.addWidget(self.btn)
        self.btn.clicked.connect(self.toggle_selection)

        self.setLayout(layout)

    def toggle_selection(self):
        cmds.select(clear=True)
        cmds.select(self.selected_objects, replace=True)


def main():
    if cmds.window('myCustomWidgetUIId', q=1, exists=True):
        cmds.deleteUI('myCustomWidgetUIId')
    if cmds.windowPref('myCustomWidgetUIId', exists=True):
        cmds.windowPref('myCustomWidgetUIId', remove=True)
    global myUI
    myUI = MyCustomWidget()
    myUI.show()

main()