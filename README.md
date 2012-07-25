VideoBrowser
============

A tiny browser for videos stored on your local disc. Created especially for slow and old computers.

Dependencies

    a Video-Player of your choice (Totem is used by default)
    ffmpeg (for thumbnails)
    python 2.6 + pygtk

Installation

It's not necessary to install the software. You just need to make VideoBrowser.py executable. Afterwards you can start it via

python VideoBrowser.py

or

/Pfad/zu/VideoBrowser.py

Configuration

At the first start a folder .VideoBrowser is create in your home directory. Thumbnails are cached and the config file is stored within this folder. The config file allows you to define values like the default video player or directories that should be used (e.g. for thumbnails).

Control

The default controls are:

    Rotate left right: cursor key left & right
    Play: space
    Quit: ‘q’ or ESC

The keys can be changed via the config file.
