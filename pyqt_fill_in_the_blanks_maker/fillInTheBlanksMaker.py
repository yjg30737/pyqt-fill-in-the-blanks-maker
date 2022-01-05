from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextEdit, QHBoxLayout, QWidget, QVBoxLayout, QApplication

from pyqt_fill_in_the_blanks_maker.fillInTheBlanksTextBrowser import FillInTheBlanksTextBrowser


class FillInTheBlanksMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__keywordsInputTextEdit = QTextEdit()
        self.__keywordsInputTextEdit.textChanged.connect(self.__setUnderline)
        self.__resultBrowser = FillInTheBlanksTextBrowser()

        lay = QHBoxLayout()
        lay.addWidget(self.__keywordsInputTextEdit)
        lay.addWidget(self.__resultBrowser)

        bottomWidget = QWidget()
        bottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(bottomWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

    def __setUnderline(self):
        keywords = self.__keywordsInputTextEdit.toPlainText().split(',')
        self.__resultBrowser.setKeywordsUnderline(keywords)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    example = FillInTheBlanksMaker()
    example.show()
    sys.exit(app.exec_())