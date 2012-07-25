import pygtk
pygtk.require('2.0')
import gtk

class Movie:

    def __init__(self,movie_name,path,snapshot):
        self.__snapshot = snapshot
        self.__movie_name = movie_name
        self.__path = path
        return
        
    def set_snapshot(self,snapshot=gtk.Image()):
        self.__snapshot = snapshot
        return
        
    def set_movie_name(self,movie_name=""):
        self.__movie_name = movie_name
        return
        
    def set_path(self,path=""):
        self.__path = path
        return
        
    def get_snapshot(self):
        return self.__snapshot
        
    def get_movie_name(self):
        return self.__movie_name
        
    def get_path(self):
        return self.__path
