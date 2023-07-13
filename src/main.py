from PyQt5.QtWidgets import QWidget, QHBoxLayout, \
    QVBoxLayout, QApplication, QTextEdit, QPushButton, QCheckBox, QDialog, QListWidgetItem

from promptLv1Widget import PromptLv1Widget
from promptLv2Widget import PromptLv2Widget
from script import PromptBuilder
from inputDialog import InputDialog


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
        self.__promptLv2Widget.added.connect(self.__lv2Added)
        self.__promptLv2Widget.deleted.connect(self.__lv2Deleted)
        self.__listWidget2 = self.__promptLv2Widget.getListWidget()

        self.__promptLv1Widget = PromptLv1Widget()

        self.__listWidget1 = self.__promptLv1Widget.getListWidget()
        self.__listWidget1.addItems(PromptBuilder.PROMPT_DICT.keys())
        self.__listWidget1.currentRowChanged.connect(self.__currentRowChanged)
        self.__listWidget1.setCurrentRow(0)
        self.__listWidget1.checkedSignal.connect(self.__generatePrompt)

        self.__promptLv1Widget.added.connect(self.__lv1Added)
        self.__promptLv1Widget.deleted.connect(self.__lv1Deleted)

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
        item = self.__listWidget1.item(r)
        if item:
            self.__listWidget2.addItems(PromptBuilder.PROMPT_DICT[item.text()])
            self.__listWidget2.setCurrentRow(0)

    def __generatePrompt(self, i, state):
        rows1 = self.__listWidget1.getCheckedRows()
        rand_arr = []
        for i in rows1:
            item = self.__listWidget1.item(i)
            if item:
                values = PromptBuilder.PROMPT_DICT[item.text()]
                rand_arr.append(values)

        self.__prompt.setText(self.__promptBuilder.generate_random_prompt(rand_arr))

    def __lv1Added(self):
        dialog = InputDialog(title='New')
        reply = dialog.exec()
        if reply == QDialog.Accepted:
            new_attr = dialog.getText()
            self.__listWidget1.addItem(QListWidgetItem(new_attr))
            self.__promptBuilder.PROMPT_DICT[new_attr] = []
    def __lv1Deleted(self):
        lv1_attrs = [self.__listWidget1.item(i).text() for i in self.__listWidget1.getCheckedRows()]
        self.__listWidget1.removeCheckedRows()
        for lv1_attr in lv1_attrs:
            del self.__promptBuilder.PROMPT_DICT[lv1_attr]

    def __lv2Added(self):
        dialog = InputDialog(title='New')
        reply = dialog.exec()
        if reply == QDialog.Accepted:
            new_attr = dialog.getText()
            lv1_item = self.__listWidget1.currentItem()
            if lv1_item:
                self.__listWidget2.addItem(QListWidgetItem(new_attr))
                self.__promptBuilder.PROMPT_DICT[lv1_item.text()].append(new_attr)

    def __lv2Deleted(self):
        lv2_cur_row = self.__listWidget2.currentRow()
        if lv2_cur_row != -1:
            lv2_item = self.__listWidget2.takeItem(lv2_cur_row)
            lv1_item = self.__listWidget1.currentItem()
            if lv1_item:
                self.__promptBuilder.PROMPT_DICT[lv1_item.text()].remove(lv2_item.text())

    def __shuffle(self):
        self.__generatePrompt(None, None)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = PromptWidget()
    w.show()
    sys.exit(app.exec())
