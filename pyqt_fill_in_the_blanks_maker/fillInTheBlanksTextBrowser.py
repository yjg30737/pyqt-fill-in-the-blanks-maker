from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat, QTextCursor
from PyQt5.QtWidgets import QTextBrowser


class FillInTheBlanksTextBrowser(QTextBrowser):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setText('Returns a copy of the rectangle that is translated offset.x() '
                     'along the x axis and offset.y() along the y axis, '
                     'relative to the current position.')

    def __selectionsInit(self):
        self.__selections = []

    def setKeywordsUnderline(self, keywords):
        self.__selectionsInit()
        for keyword in keywords:
            fmt = QTextCharFormat()
            fmt.setForeground(Qt.white)
            fmt.setUnderlineColor(Qt.black)
            fmt.setUnderlineStyle(QTextCharFormat.SingleUnderline)

            self.__setUnderlineFormat(fmt, keyword)
            self.__setHoverEvent(keyword)

    def __setUnderlineFormat(self, fmt, keyword):
        doc = self.document()
        cur = QTextCursor()
        while True:
            cur = doc.find(keyword, cur)
            if cur.isNull() or cur.atEnd():
                break
            sel = QTextBrowser.ExtraSelection()
            sel.cursor = cur
            sel.format = fmt
            self.__selections.append(sel)
        self.setExtraSelections(self.__selections)

    def __setHoverEvent(self, keyword: str):
        doc = self.document()
        cur = QTextCursor()