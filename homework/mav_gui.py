# .. -*- coding: utf-8 -*-
#
# **********************************************************
# mav_gui.py - MAV recharging with a GUI, implemented in Qt.
# **********************************************************
#
# Imports
# =======
# Library
# -------
import sys
from os.path import dirname, join
#
# Third-party
# -----------
# Use "Pythonic" (and PyQt5-compatible) `glue classes <http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html>`_. This must be done before importing from PyQt4.
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import uic
#
# Implement a dialog box.
# =======================
class MyDialog(QDialog):
    def __init__(self):
        # First, let the QDialog initialize itself.
        super(MyDialog, self).__init__()

        # `Load <http://pyqt.sourceforge.net/Docs/PyQt4/designer.html#PyQt4.uic.loadUi>`_ in our UI. The secord parameter lods the resulting UI directly into this class.
        uic.loadUi(join(dirname(__file__), 'mav_gui.ui'), self)
#
# Main
# ====
def main():
    # Initialize the program. A `QApplication <http://doc.qt.io/qt-4.8/qapplication.html>`_ must always be created.
    qa = QApplication(sys.argv)
    # Construct the UI: either a `QDialog <http://doc.qt.io/qt-4.8/qdialog.html>`_ or a `QMainWindow <http://doc.qt.io/qt-4.8/qmainwindow.html>`_.
    md = MyDialog()
    # The UI is hidden while it's being set up. Now that it's ready, it must be manually shown.
    md.show()

    # Main loop.
    qa.exec_()

if __name__ == '__main__':
    main()
