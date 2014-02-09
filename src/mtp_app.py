#!/usr/bin/python3
import sys
from gi.repository import Gtk
import logging
from RunLoggingHandlerTextBuffer import RunLoggingHandlerTextBuffer


class mtp_app:

    def on_window_destroy(self, widget, data=None):
        Gtk.main_quit()

    def on_switch1_activate(self, widget, data=None, extra=None):
        switcher_state = not self.switcher.get_active()
        self._log.debug("Estado [" + str(switcher_state) + "]")
        if (self.connection_state and not switcher_state):
            self._log.debug("Deactivating")
        elif (not self.connection_state and switcher_state):
            self._log.debug("Activating")
        else:
            self._log.debug("No change")
        # last but not least
        self.connection_state = switcher_state

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("../glade_files/main_window.glade")
  # get a pointer to the graphical objects.
        self.window = builder.get_object("window1")
        self.switcher = builder.get_object("switch1")
        self.logging_view = builder.get_object("logging")
        self.logging_view_buffer = self.logging_view.get_buffer()
        self.logging_view = builder.get_object("messaging")
        self.messaging_view_buffer = self.logging_view.get_buffer()
        self.status_bar = builder.get_object("statusbar")
# Tell the handler where to send its output
        # and get a pointer to it.
        self.lvh = RunLoggingHandlerTextBuffer(self.logging_view_buffer)
        # I will use a second RungLoggingHandlres for messages
        self.mvh = RunLoggingHandlerTextBuffer(self.messaging_view_buffer)
        
        #Activate some basic configuration in the loggin system
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    stream=self.lvh
                    )
                    #NO FILE FOR THE MOMENT
                    #,filename='/tmp/myapp.log',
                    #filemode='w')
                    
        #Get a logger.
        self._log = logging.getLogger(__name__)
        #self._log.addHandler(self.lvh)
        #self._log.setLevel(logging.DEBUG)
        #self.logging_view_buffer.insert_at_cursor("hola")
        self._log.debug("Arrancando3")
        builder.connect_signals(self)
        #self.switcher.connect("button-press-event",self.on_switch1_activate,None)
        self.switcher.set_active(True)
        self._log.debug("Arrancando4")
        self.mvh.writeln("Arrancado!!")
        self.mvh.writeln("Arrancado2!!")
        self.connection_state = (False)
        self.switcher.set_active(self.connection_state)
        self._log.debug("Arrancando4")
        #the state of the swithcer is the negated wone from the graph think
        switcher_state = not self.switcher.get_active()
        self._log.debug("Estado [" + str(switcher_state) + "] int[" + str(self.connection_state) + "]" )


if __name__ == "__main__":
    editor = mtp_app()
    editor.window.show()
    Gtk.main()
    sys.exit(1)
