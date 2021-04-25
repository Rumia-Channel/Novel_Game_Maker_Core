# coding: UTF-8

import os
import sys
import json
import pathlib
from PySide2 import QtWidgets as qw

GameSetting = open('setting/setting.json', 'r')
GameSetting_Load = json.load(GameSetting) 

GameTitle = GameSetting_Load['StartUp']['Title']

# ウィンドウの見た目と各機能（今はウィンドウだけ）
class MainWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(GameTitle)

# アプリの実行と終了
app = qw.QApplication()
window = MainWindow()
window.show()
app.exec_()

