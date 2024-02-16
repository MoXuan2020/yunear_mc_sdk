class Event(object):

    def __init__(self, callback):
        self.callback = callback
        self.mod = None
        self.args = None

    def __call__(self, args=None):
        self.args = args
        self.callback(self.mod, self)

    def bind_mod(self, mod):
        self.mod = mod
