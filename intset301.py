import abc

class IntSet301:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add(self, x):
        """Adds x to this set if it is not already present."""
        return

    @abc.abstractmethod
    def remove(self, x):
        """Removes x from this set it is is present."""
        return

    @abc.abstractmethod
    def contains(self, x):
        """Determines if this set contains x."""
        return false

    @abc.abstractmethod
    def size(self):
        """Determines this size of this set."""
        return 0

    @abc.abstractmethod
    def next_excluded(self, x):
        """Returns the smallest integer greater than or equal to x that
           is not in this set.
        """
        return x
