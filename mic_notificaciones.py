#!/usr/bin/env python2
import gi.repository.GLib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gi
import os
import sys
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1') 
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

import signal

APPINDICATOR_ID = 'myappindicator'
CURRPATH = os.path.dirname(os.path.realpath(__file__))

class Indicator():

    def __init__(self):
        DBusGMainLoop(set_as_default=True)
        print(sys.argv[1])
        bus = dbus.SessionBus()
        bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
        bus.add_message_filter(self.notifications)
        devicename=sys.argv[1]
        device= os.popen('arecord -l | gawk -v b=\''+devicename+'\' \'match($0, b, a) {print}\' | gawk \'$2 {print $2}\'')
        state = os.popen('amixer -c '+device.read().strip().replace(":","")+' get Mic | gawk \'match($0, /Capture .*\[(.*)\]/, a) {print a[1]}\'')
        if state.read().find('on') > -1:
            icon = "/microphone-on.png"
        else:
            icon = "/microphone-off.png"
        self.indicator = appindicator.Indicator.new(APPINDICATOR_ID, CURRPATH+icon, appindicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())
        #gtk.main()

    def build_menu(self):
        menu = gtk.Menu()
        item_mic = gtk.MenuItem('Mic On/Off')
        item_quit = gtk.MenuItem('Quit')
        item_mic.connect('activate', self.mic_toggle)
        item_quit.connect('activate', self.quit)
        menu.append(item_mic)
        menu.append(item_quit)
        menu.show_all()
        return menu

    def notifications(self, bus, message):
        # do your magic
        for arg in message.get_args_list():
            if (type(arg) == dbus.String):
                if (str(arg).find('Mic switched: on') > -1):
                    self.indicator.set_icon(CURRPATH+"/microphone-on.png")

                if (str(arg).find('Mic switched: off') > -1):
                    self.indicator.set_icon(CURRPATH+"/microphone-off.png")

    def mic_toggle(self, source):
        os.popen('/home/ricardo/mic_control.sh '+ sys.argv[1])


    def mic_on(self, source):
        self.indicator.set_icon(CURRPATH+"/microphone-on.png")

    def mic_off(self, source):
        self.indicator.set_icon(CURRPATH+"/microphone-off.png")

    def quit(self, source):
        gtk.main_quit()

if __name__ == "__main__":
    
    

    #mainloop = gi.repository.GLib.MainLoop()
    #mainloop.run()
    Indicator()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()
    # main()
