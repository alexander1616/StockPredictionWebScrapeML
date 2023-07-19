import time

def _timer(func):
    def alex(*arg, **kwarg):
        start = time.time()
        xxx = func(*arg, **kwarg)
        end = time.time()
        #string formatting 16.6, %param
        print("%16.6f" %(end - start))
        return xxx
    return alex

class Timer:
    def __init__(self, tag = None):
        self._starttsp = 0
        self._endtsp = 0
        if tag is None:
            self._tag = ""
        else:
            self._tag = tag

    def __repr__(self):
        return "%s: %16.6f"%(self._tag, self.diff())
    
    def start(self):
        self._starttsp = time.time()

    def end(self):
        self._endtsp = time.time()

    def diff(self):
        return self._endtsp - self._starttsp
