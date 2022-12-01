import base64
import logging

logger = None
_stream_handler = None
_file_handler = None
_handlers = []

def get_logger():
    global logger
    return logger


def write_log(s):
    global logger
    if logger:
        logger.info(s)
        
        
def use_logging(name=None,
                stdout=True,
                fout=False,
                fpath=None,
                fmt=None,
                init=True,
                mode='a'):
    
    global logger
    global _stream_handler
    global _file_handler
    global _handlers
    
    if not name:
        name = "test"
    
    if init:
        for handler in _handlers:        
            handler.close()
            logger.removeHandler(handler)
            
        logger = None
        
    if not logger:
        # Create logger
        logger = logging.getLogger(name)        
        
        # Formatting
        if not fmt:
            fmt = "[%(asctime)s] %(message)s"                                      
        formatter = logging.Formatter(fmt, "%Y-%m-%d %H:%M:%S")  
        
        # Standard output
        if stdout:
            _stream_handler = logging.StreamHandler()
            _stream_handler.setFormatter(formatter)
            logger.addHandler(_stream_handler)
            _handlers.append(_stream_handler)
        
        # File output
        if fout:
            if not fpath:
                fpath = "%s.log"%(name)
            _file_handler = logging.FileHandler(fpath, mode=mode)
            _file_handler.setFormatter(formatter)
            logger.addHandler(_file_handler)
            _handlers.append(_file_handler)
                
        # Set log level
        logger.setLevel(logging.INFO)
        
    return logger


def finish_logging():
    
    global logger
    global _stream_handler
    global _file_handler
    
    for handler in _handlers:        
        handler.close()
        logger.removeHandler(handler)
        


def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def decode(s):
    return base64.b64decode(s).decode()

def uformat(raw, ep):
    return decode(raw).format(decode(ep))


def to_json(response):
    try:
        res = response.json()
    except Exception as err:
        raise RuntimeError("[SYSTEM ERROR] %s"%(response))
    
    return res
