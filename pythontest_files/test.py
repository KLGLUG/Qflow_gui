#!/usr/bin/python
# -*- coding: utf-8 -*-
from gi.repository import Gtk
class Handler:
def button_1clicked(self, button):
print "Hello, World!"
builder = Gtk.Builder()
builder.add_from_file("myprogram.glade")
builder.connect_signals(Handler())
ournewbutton = builder.get_object("button1")
ournewbutton.set_label("Hello, World!")
window = builder.get_object("window1")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

