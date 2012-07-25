import ConfigParser
import os

class ConfigManager:

    def __init__(self, configfilepath):
        self.config = ConfigParser.RawConfigParser()
        if not os.path.exists(configfilepath):
            os.makedirs(configfilepath.rpartition('/')[0])
            self._set_defaults(configfilepath)
        self._load_config(configfilepath)

    def get_value(self,section,key):
        return self.config.get(section,key)

    def _load_config(self,configfile):
        self.config.readfp(open(configfile))
        return

    def _set_defaults(self,configfilepath):
        self.config.add_section('FileSystem')
        self.config.add_section('Keys')
        self.config.add_section('External')
        self.config.add_section('Appearance')
        self.config.set('FileSystem','moviedir',os.environ['HOME']+'/Videos')
        self.config.set('FileSystem','cachedir',os.environ['HOME']+'/.VideoBrowser/cache')
        self.config.set('Keys','left', '65363') # rightarrow
        self.config.set('Keys','right', '65361') # leftarrow
        self.config.set('Keys','play', '32') # space
        self.config.set('Keys','quit1', '113') # q
        self.config.set('Keys','quit2', '65307') # esc
        self.config.set('External', 'player', '/usr/bin/totem --fullscreen')
#        self.config.set('External', 'ffmpeg', '/usr/bin/ffmpeg')
        self.config.set('Appearance', 'bg_image', os.getcwd()+'/bg.png')
        self.config.set('Appearance', 'font_small', '10')
        self.config.set('Appearance', 'font_big', '15')
        self.config.set('Appearance', 'fullscreen', 'true')
        self.config.set('Appearance', 'font_color', 'white')
#        self.config.set('Appearance', 'thumbnail_size_small', '240x180')        
#        self.config.set('Appearance', 'thumbnail_size_big', '320x240')
        with open(configfilepath, 'wb') as configfile:
            self.config.write(configfile)

