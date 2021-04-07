#!/usr/bin/env python3

import configparser
import gi
import os
import threading

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

class SetThemeWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Set GTK3 Theme", border_width=10)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)
        self.add(stack)

        label = Gtk.Label()
        label.set_markup("<big>Theme</big>")
        stack.add_titled(label, "theme", "Theme")
        label = Gtk.Label()
        label.set_markup("<big>Font</big>")
        stack.add_titled(label, "font", "Font")

        stack_switcher = Gtk.StackSwitcher(stack=stack)

        hb = Gtk.HeaderBar(title="Set GTK3 Theme", show_close_button=True)
        self.set_titlebar(hb)
        hb.pack_start(stack_switcher)

        save_button = Gtk.Button()
        save_button.add(self._get_button_icon("document-save-symbolic"))
        save_button.connect("clicked", self.set_gtk3_theme)
        hb.pack_end(save_button)

        reset_button = Gtk.Button()
        reset_button.add(self._get_button_icon("document-revert-symbolic"))
        reset_button.connect("clicked", self.reset_current_config)
        hb.pack_end(reset_button)

    def _get_button_icon(self, icon):
        return Gtk.Image.new_from_gicon(Gio.ThemedIcon(name=icon), Gtk.IconSize.BUTTON)

    def reset_current_config(self, widget):
        pass

    def read_current_config(self, widget):
        pass

    def set_gtk3_theme(self, widgetn):
        pass

if __name__ == "__main__":
    win = SetThemeWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()