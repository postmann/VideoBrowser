#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os

from Data import Data
from Gui import Gui
from ConfigManager import ConfigManager
	
class VideoBrowser:

    def __init__(self):
        self.config = ConfigManager(os.environ['HOME']+'/.VideoBrowser/VideoBrowser.conf')
        self.data = Data(self.config.get_value('FileSystem','moviedir'),self.config.get_value('FileSystem','cachedir'))
        self.files = self.data.get_files("avi")
        self.gui = Gui(self.files)

    def main(self):
        gtk.main()
        return

if __name__ == "__main__":
    videoBrowser = VideoBrowser()
    videoBrowser.main()
