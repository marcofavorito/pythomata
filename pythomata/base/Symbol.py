# -*- coding: utf-8 -*-


class Symbol(object):
    """A class to represent a symbol (actually, a wrap for a string)"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def _members(self):
        return (self.name)

    def __eq__(self, other):
        if type(other) is type(self):
            return self._members() == other._members()
        else:
            return False

    def __hash__(self):
        return hash(self._members())

    def __repr__(self):
        return ", ".join(map(str,self._members()))

    def __lt__(self, other):
        return self.name.__lt__(other.name)
