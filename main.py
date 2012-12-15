#!/usr/bin/env python
#-*- coding:utf-8 -*-

from gi.repository import Gtk
from ui import ui

class Waterloo ():
    def __init__(self):
        self.builder=Gtk.Builder()
        self.glade="waterloo.glade"
        self.builder.add_from_file(self.glade)
        self.ui=ui(self.builder)
        
        self.builder.connect_signals(self)
        self.ui['waterloo_main'].set_resizable(False)
        
        self.ui['waterloo_main'].show_all()
        self.ui['waterloo_main'].connect("delete-event", Gtk.main_quit)
        
        Gtk.main()
        
if __name__=='__main__':
    Waterloo()
