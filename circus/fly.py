from subprocess import Popen
import time


class Fly(object):
    def __init__(self, wid, cmd):
        self.wid = str(wid)
        self.cmd = cmd.replace('$WID', self.wid)
        self._worker = Popen(self.cmd.split())
        self.started = time.time()

    def poll(self):
        return self._worker.poll()

    def terminate(self):
        return self._worker.terminate()

    def age(self):
        return time.time() - self.started

    @property
    def pid(self):
        return self._worker.pid



