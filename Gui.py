import pygtk
pygtk.require('2.0')
import gtk
import os

from ConfigManager import ConfigManager

class Gui:

    def __init__(self,files):
        self.files = files

        self.config = ConfigManager(os.environ['HOME']+'/.VideoBrowser/VideoBrowser.conf')

        pixbuf = gtk.gdk.pixbuf_new_from_file(self.config.get_value('Appearance','bg_image'))
        pixmap, mask = pixbuf.render_pixmap_and_mask()
        width, height = pixmap.get_size()
        del pixbuf

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_app_paintable(True) 
        if self.config.get_value('Appearance','fullscreen') == "true":
            self.window.fullscreen()
        else:
            self.window.resize(width, height)
        self.window.realize()
        self.window.window.set_back_pixmap(pixmap, False)
        del pixmap
        self.window.set_keep_above(True)
        self.window.connect("destroy",gtk.main_quit)
        self.window.connect("key_press_event",self.key_pressed)
        
        self.table = gtk.Table(3,2,False)

        self.set_guiobjects()

        self.window.add(self.table)
        self.table.show()
        self.window.show()

    def rotate_right(self,widget,data=None):
        self.files.insert(0,self.files.pop())
        self.reset_images()

    def rotate_left(self,widget,data=None):
        self.files.reverse()
        self.files.insert(0,self.files.pop())
        self.files.reverse()
        self.reset_images()

    def reset_images(self):
        children = self.table.get_children()
        for i in children:
            if type(i).__name__ == 'EventBox':
                for j in i.get_children():
                    i.remove(j)
            self.table.remove(i)
        self.set_guiobjects()

    def key_pressed(self,widget,data=None):
        if str(data.keyval) == self.config.get_value('Keys','right'):
            self.rotate_right(self)
        elif str(data.keyval) == self.config.get_value('Keys','left'):
            self.rotate_left(self)
        elif str(data.keyval) == self.config.get_value('Keys','quit1') or str(data.keyval) == self.config.get_value('Keys','quit2'):
            gtk.main_quit()
        elif str(data.keyval) == self.config.get_value('Keys','play'):
            self.play_video(self)
#        else:
#            print "Key pressed:", data.keyval
            
    def set_guiobjects(self):
        if len(self.files) > 2:
            show = 3
        else:
            show = len(self.files)
        for i in range(show):
            label = gtk.Label()
            eventbox = gtk.EventBox()
            eventbox.set_visible_window(False)
            if i != 1:
                tmp_image = self.__getGtkImage(self.files[i], 240, 180)
                tmp_image.show()
                eventbox.add(tmp_image)
                if i == 0:
                    eventbox.connect("button_press_event",self.rotate_right)
                else:
                    eventbox.connect("button_press_event",self.rotate_left)
                if len(self.files[i].get_movie_name()) > 40:
                    label.set_markup('<span color="'+self.config.get_value('Appearance','font_color')+'" size="'+self.config.get_value('Appearance','font_small')+'000">'+self.files[i].get_movie_name()[:40]+"..."+'</span>')
                else:
                    label.set_markup('<span color="'+self.config.get_value('Appearance','font_color')+'" size="'+self.config.get_value('Appearance','font_small')+'000">'+self.files[i].get_movie_name()+'</span>')
            else:
                tmp_image = self.__getGtkImage(self.files[i], 320,240)
                tmp_image.show()
                eventbox.add(tmp_image)
                eventbox.connect("button_press_event",self.play_video)
                if len(self.files[i].get_movie_name()) > 40:
                    label.set_markup('<span color="'+self.config.get_value('Appearance','font_color')+'" size="'+self.config.get_value('Appearance','font_big')+'000">'+self.files[i].get_movie_name()[:40]+"..."+'</span>')
                else:
                    label.set_markup('<span color="white" size="15000">'+self.files[i].get_movie_name()+'</span>')
            eventbox.show()
            self.table.attach(eventbox,i,i+1,0,1)
            label.show()
            self.table.attach(label,i,i+1,1,2)

    def __getGtkImage(self, image_file, sizeX, sizeY):
            tmp_image = gtk.Image()
            try:
                tmp_pixbuf = image_file.get_snapshot().get_pixbuf().scale_simple(sizeX,sizeY,gtk.gdk.INTERP_HYPER)
                tmp_image.set_from_pixbuf(tmp_pixbuf)
            except ValueError:
                print "Could not set thumbnail for file "+image_file.get_movie_name()+"!"
            return tmp_image
    
    def play_video(self,widget,data=None):
        os.system(self.config.get_value('External','player')+" \""+self.files[1].get_path()+"/"+self.files[1].get_movie_name()+".avi\"")
