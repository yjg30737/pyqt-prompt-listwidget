from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QAbstractItemView, QWidget, QCheckBox, QHBoxLayout, QSpacerItem, \
    QSizePolicy, QVBoxLayout

from check_listwidget import CheckBoxListWidget
from svgButton import SvgButton


class PromptLv1Widget(QWidget):
    added = pyqtSignal()
    deleted = pyqtSignal()

    def __init__(self):
        super(PromptLv1Widget, self).__init__()
        self.__initUi()
        
    def __initUi(self):
        allCheckBox = QCheckBox('Check all')

        self.__listWidget = CheckBoxListWidget()
        self.__listWidget.setDragDropMode(QAbstractItemView.InternalMove)

        self.__addBtn = SvgButton(self)
        self.__delBtn = SvgButton(self)

        self.__addBtn.setIcon('ico/add.svg')
        self.__delBtn.setIcon('ico/delete.svg')

        self.__addBtn.setToolTip('Add')
        self.__delBtn.setToolTip('Delete')

        self.__addBtn.clicked.connect(self.__addClicked)
        self.__delBtn.clicked.connect(self.__deleteClicked)

        allCheckBox.stateChanged.connect(self.__listWidget.toggleState)

        lay = QHBoxLayout()
        lay.addWidget(allCheckBox)
        lay.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.MinimumExpanding))
        lay.addWidget(self.__addBtn)
        lay.addWidget(self.__delBtn)
        lay.setAlignment(Qt.AlignRight)
        lay.setContentsMargins(0, 0, 0, 0)
        btnWidget = QWidget()
        btnWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(btnWidget)
        lay.addWidget(self.__listWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)
        
    def getListWidget(self):
        return self.__listWidget

    def __addClicked(self):
        self.added.emit()

    def __deleteClicked(self):
        self.deleted.emit()
