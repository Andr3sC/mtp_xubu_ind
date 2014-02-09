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
        builder.add_from_file("glade_files/main_window.xml")
        self.window = builder.get_object("window1")
        self.switcher = builder.get_object("switch1")
        self.text_view = builder.get_object("textview1")
        self.tb = self.text_view.get_buffer()
        self.tlh = RunLoggingHandlerTextBuffer(self.tb)
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M',
                            stream=self.tlh
                            )
        #,filename='/tmp/myapp.log',
        # filemode='w')
        self._log = logging.getLogger(__name__)
        # self._log.addHandler(self.tlh)
        # self._log.setLevel(logging.DEBUG)
        # self.tb.insert_at_cursor("hola")
        self._log.debug("Arrancando3")
        builder.connect_signals(self)
        # self.switcher.connect("button-press-event" ,
        # self.on_switch1_activate,None)
        self.connection_state = (False)
        self.switcher.set_active(self.connection_state)
        self._log.debug("Arrancando4")
        switcher_state = not self.switcher.get_active()
        self._log.debug("Estado [" + str(switcher_state) + "]")


if __name__ == "__main__":
    editor = mtp_app()
    editor.window.show()
    Gtk.main()
    sys.exit(1)
