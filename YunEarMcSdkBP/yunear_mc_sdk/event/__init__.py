class Event(object):

    def __init__(self, callback):
        self.callback = callback
        self.mod = None

    def __call__(self, args):
        self.callback(self.mod, args)

    def bind_mod(self, mod):
        self.mod = mod
