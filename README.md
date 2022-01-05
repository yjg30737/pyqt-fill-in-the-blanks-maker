# pyqt-fill-in-the-blanks-maker
PyQt fill in the blanks maker

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-fill-in-the-blanks-maker.git --upgrade```

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_fill_in_the_blanks_maker.fillInTheBlanksMaker import FillInTheBlanksMaker


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = FillInTheBlanksMaker()
    ex.show()
    app.exec_()
```

Result

Before

![image](https://user-images.githubusercontent.com/55078043/148306133-5db34732-1541-4e49-ad4e-52457c262915.png)

After

![image](https://user-images.githubusercontent.com/55078043/148306184-2b3c5002-c38f-45ac-80fa-d1bafc7b6876.png)
