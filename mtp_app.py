#!/usr/bin/python3
import sys
from gi.repository import Gtk
import logging
	
class mtp_app:

    def on_window_destroy(self, widget, data=None):
        self._log.debug("Antes de quit on window destroy")
        Gtk.main_quit()
        #sys.exit(1)
        self._log.debug("Tras de quit on window destroy")
     
    def on_switch1_activate(self, widget, data=None, extra=None):
        self._log.debug("Antes de quit switch_change")
        Gtk.main_quit()
        self._log.debug("Despues de quit switch_change")
 
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/tmp/myapp.log',
                    filemode='w')
        self._log = logging.getLogger(__name__)
        self._log.info("Arrancando")
        builder = Gtk.Builder()
        self._log.debug("Arrancando1")
        builder.add_from_file("glade_files/main_window.xml") 
        self._log.debug("Arrancando2")
        
        self.window = builder.get_object("window1")
        self.switcher = builder.get_object("switch1")
        self._log.debug("Arrancando3")
        builder.connect_signals(self)       
        #self.switcher.connect("button-press-event",self.on_switch1_activate,None)
        self.switcher.set_active(True)
        self._log.debug("Arrancando4")
    
if __name__ == "__main__":
    editor = mtp_app()
    editor.window.show()
    Gtk.main()
    sys.exit(1)

