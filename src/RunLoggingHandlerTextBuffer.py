import logging
import sys


class RunLoggingHandlerTextBuffer(logging.Handler):

    """Log against selected textBuffer, so we can include it on a
    a graphical interface"""

    def __init__(self, textbuffer):
        logging.Handler.__init__(self)
        self.textbuffer = textbuffer

    def utf8conv(self, x):
        try:
            return unicode(x, 'utf8')
        except:
            return x

    def writeln(self, record):
        self.textbuffer.insert_at_cursor(record +'\n') 

    def write(self, record):
        self.textbuffer.insert_at_cursor(record)    # + '\n')

    def emit(self, record):
        self.textbuffer.insert_at_cursor(record.getMessage() + '\n')

if __name__ == "__main__":
    fake_tb = ""
    mylog = RunLoggingHandler(fake_tb)
    sys.exit(1)
