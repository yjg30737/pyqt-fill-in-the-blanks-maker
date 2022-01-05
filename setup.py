from setuptools import setup, find_packages

setup(
    name='pyqt-fill-in-the-blanks-maker',
    version='0.0.2',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt fill in the blanks maker',
    url='https://github.com/yjg30737/pyqt-fill-in-the-blanks-maker.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)