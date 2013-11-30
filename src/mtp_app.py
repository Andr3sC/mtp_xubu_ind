#!/usr/bin/python3
import sys
from gi.repository import Gtk
import logging

class RunLoggingHandler(logging.Handler):
     def __init__(self, textbuffer):
         logging.Handler.__init__(self)
         self.textbuffer = textbuffer

     def utf8conv(self,x):
         try:
             return unicode(x,'utf8')
         except:
             return x

     def write(self, record):
        self.textbuffer.insert_at_cursor(record)#+'\n') 
        
     def emit(self, record):
         self.textbuffer.insert_at_cursor(record.getMessage()+'\n') 
         	
class mtp_app:

    def on_window_destroy(self, widget, data=None):
        Gtk.main_quit()
     
    def on_switch1_activate(self, widget, data=None, extra=None):
        self._log.debug("Estado ["+str(self.switcher.get_active())+"]")
        
 
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("../glade_files/main_window.glade") 
        
        self.window = builder.get_object("window1")
        self.switcher = builder.get_object("switch1")
        self.text_view = builder.get_object("textview1")
        self.tb = self.text_view.get_buffer()
        self.tlh = RunLoggingHandler(self.tb)
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    stream=self.tlh
                    )
                    #,filename='/tmp/myapp.log',
                    #filemode='w')
        self._log = logging.getLogger(__name__)
        #self._log.addHandler(self.tlh) 
        #self._log.setLevel(logging.DEBUG)
        #self.tb.insert_at_cursor("hola")
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

