# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Jul  6 13:45:26 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1191, 639)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setEnabled(False)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.graphicsView = QtGui.QGraphicsView(self.tab)
        self.graphicsView.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.show_null = QtGui.QCheckBox(self.groupBox)
        self.show_null.setGeometry(QtCore.QRect(17, 25, 125, 16))
        self.show_null.setObjectName(_fromUtf8("show_null"))
        self.show_pointers = QtGui.QCheckBox(self.groupBox)
        self.show_pointers.setGeometry(QtCore.QRect(17, 45, 125, 16))
        self.show_pointers.setObjectName(_fromUtf8("show_pointers"))
        self.show_search = QtGui.QCheckBox(self.groupBox)
        self.show_search.setEnabled(False)
        self.show_search.setGeometry(QtCore.QRect(590, 0, 161, 36))
        self.show_search.setObjectName(_fromUtf8("show_search"))
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.tab_search_structures = QtGui.QToolBox(self.tab)
        self.tab_search_structures.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_search_structures.sizePolicy().hasHeightForWidth())
        self.tab_search_structures.setSizePolicy(sizePolicy)
        self.tab_search_structures.setObjectName(_fromUtf8("tab_search_structures"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 571, 383))
        self.page.setObjectName(_fromUtf8("page"))
        self.columnView = QtGui.QColumnView(self.page)
        self.columnView.setGeometry(QtCore.QRect(0, -10, 291, 401))
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(70, 10, 67, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.tab_search_structures.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 571, 383))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.tab_search_structures.addItem(self.page_2, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tab_search_structures, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setEnabled(False)
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1191, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSearch = QtGui.QMenu(self.menubar)
        self.menuSearch.setObjectName(_fromUtf8("menuSearch"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menu_file_open = QtGui.QAction(MainWindow)
        self.menu_file_open.setObjectName(_fromUtf8("menu_file_open"))
        self.menu_file_exit = QtGui.QAction(MainWindow)
        self.menu_file_exit.setObjectName(_fromUtf8("menu_file_exit"))
        self.actionSearch_Structure = QtGui.QAction(MainWindow)
        self.actionSearch_Structure.setObjectName(_fromUtf8("actionSearch_Structure"))
        self.menu_search_value = QtGui.QAction(MainWindow)
        self.menu_search_value.setObjectName(_fromUtf8("menu_search_value"))
        self.menu_search_structure = QtGui.QAction(MainWindow)
        self.menu_search_structure.setObjectName(_fromUtf8("menu_search_structure"))
        self.menuFile.addAction(self.menu_file_open)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_file_exit)
        self.menuSearch.addAction(self.menu_search_structure)
        self.menuSearch.addAction(self.menu_search_value)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tab_search_structures.setCurrentIndex(0)
        QtCore.QObject.connect(self.menu_file_exit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Haystack Memory analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Highlight", None, QtGui.QApplication.UnicodeUTF8))
        self.show_null.setText(QtGui.QApplication.translate("MainWindow", "Null values", None, QtGui.QApplication.UnicodeUTF8))
        self.show_pointers.setText(QtGui.QApplication.translate("MainWindow", "Pointer values", None, QtGui.QApplication.UnicodeUTF8))
        self.show_search.setText(QtGui.QApplication.translate("MainWindow", "Find session_state", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_search_structures.setItemText(self.tab_search_structures.indexOf(self.page), QtGui.QApplication.translate("MainWindow", "Page 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_search_structures.setItemText(self.tab_search_structures.indexOf(self.page_2), QtGui.QApplication.translate("MainWindow", "Page 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSearch.setTitle(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_open.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_open.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open a memory dump", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_exit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_exit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Exit Application", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file_exit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch_Structure.setText(QtGui.QApplication.translate("MainWindow", "Search Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_search_value.setText(QtGui.QApplication.translate("MainWindow", "Search value", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_search_structure.setText(QtGui.QApplication.translate("MainWindow", "Search Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_search_structure.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))

