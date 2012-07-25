import pygtk
pygtk.require('2.0')
import gtk
import commands
import os
import re
from random import randint

from Movie import Movie


class Data:

    def __init__(self,vid_dir,cache_dir):
        self.vid_dir = vid_dir
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        return

    def get_files(self,filter=""):
        # get all files
        file_list = []
        for root_dir, sub_folders, files in os.walk(self.vid_dir):
            # filter files
            if filter != "":
                files = self.__filter_files(files,filter)
            for file in files:
                movie = Movie(file[:len(file)-4],root_dir,self.__get_snapshot(root_dir+"/"+file))
                file_list.append(movie)
        return file_list

    def __create_snapshot(self,file):
        os.system("ffmpeg -i \""+file+"\" -f image2 -t 0.001 -ss "+str(randint(0,10))+" -s 320x240 \""+self.cache_dir+"/"+file.rpartition("/")[2]+".jpg\"")
        return

    def __get_snapshot(self,file):
        img = gtk.Image()
        if not os.path.exists(self.cache_dir+"/"+file.rpartition("/")[2]+".jpg"):
            self.__create_snapshot(file)
        img.set_from_file(self.cache_dir+"/"+file.rpartition("/")[2]+".jpg")
        return img

    def __filter_files(self,file_list,filter):
        result = []
        exp = re.compile(filter)
        for i in file_list:
            if exp.search(i):
                result.append(i)
        return result
