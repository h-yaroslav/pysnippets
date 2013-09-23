#!/usr/bin/python

class Parrot(object):
    """
    If then c is an instance of C,
    c.x will invoke the getter,
    c.x = value will invoke the setter and
    del c.x the deleter.
    """
    def __init__(self):
        self._voltage = 10000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        self._voltage = value

    @voltage.deleter
    def voltage(self):
        del self._voltage

if __name__ == '__main__':
    a = Parrot()
    print a.voltage
    a.voltage = 220
    print a.voltage
    #del a.voltage
    #print a.voltage

