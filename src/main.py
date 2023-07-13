from PyQt5.QtWidgets import QWidget, QHBoxLayout, \
    QVBoxLayout, QApplication, QTextEdit, QPushButton, QCheckBox

from promptLv1Widget import PromptLv1Widget
from promptLv2Widget import PromptLv2Widget
from script import PromptBuilder


class PromptWidget(QWidget):
    def __init__(self):
        super(PromptWidget, self).__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__promptBuilder = PromptBuilder()

    def __initUi(self):
        self.__weightCheckBox = QCheckBox('Apply Weight in Randomizer')
        self.__weightCheckBox.toggled.connect(self.__promptBuilder.set_weight)

        self.__prompt = QTextEdit()

        self.__promptLv2Widget = PromptLv2Widget()
        self.__listWidget2 = self.__promptLv2Widget.getListWidget()

        self.__promptLv1Widget = PromptLv1Widget()
        self.__listWidget1 = self.__promptLv1Widget.getListWidget()
        self.__listWidget1.addItems(PromptBuilder.PROMPT_DICT.keys())
        self.__listWidget1.currentRowChanged.connect(self.__currentRowChanged)
        self.__listWidget1.setCurrentRow(0)
        self.__listWidget1.checkedSignal.connect(self.__generatePrompt)

        lay = QHBoxLayout()
        lay.addWidget(self.__promptLv1Widget)
        lay.addWidget(self.__promptLv2Widget)
        lay.setContentsMargins(0, 0, 0, 0)

        topWidget = QWidget()
        topWidget.setLayout(lay)

        controlWidget = QWidget()
        self.__shuffleBtn = QPushButton('Shuffle')
        self.__shuffleBtn.clicked.connect(self.__shuffle)
        lay = QHBoxLayout()
        lay.addWidget(self.__shuffleBtn)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        controlWidget.setLayout(lay)

        bottomWidget = QWidget()
        bottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(self.__weightCheckBox)
        lay.addWidget(topWidget)
        lay.addWidget(controlWidget)
        lay.addWidget(bottomWidget)
        lay.addWidget(self.__prompt)
        self.setLayout(lay)

    def __currentRowChanged(self, r):
        self.__listWidget2.clear()
        self.__listWidget2.addItems(PromptBuilder.PROMPT_DICT[self.__listWidget1.item(r).text()])
        self.__listWidget2.setCurrentRow(0)

    def __generatePrompt(self, i, state):
        rows1 = self.__listWidget1.getCheckedRows()
        rand_arr = []
        for i in rows1:
            values = PromptBuilder.PROMPT_DICT[self.__listWidget1.item(i).text()]
            rand_arr.append(values)

        self.__prompt.setText(self.__promptBuilder.generate_random_prompt(rand_arr))

    def __shuffle(self):
        self.__generatePrompt(None, None)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = PromptWidget()
    w.show()
    sys.exit(app.exec())
